#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import ipaddr
import ConfigParser


def analy_req(address):
    main_domain = conf_read('maindomain')
    address = address[:-len(main_domain) - 1]
    payload = conf_read('payload')
    encoding = conf_read('encoding')
    record = address

    try:

        if encoding == 'int':
            record = ipaddr.IPAddress(int(address)).__str__()
        elif encoding == 'hex':
            try:
                address = address.decode('hex')

                if ipaddr.IPAddress(address).version == 4:
                    record = address
                elif conf_read('record_type') == 'AAAA' and ipaddr.IPAddress(address).version == 6:
                    record = address
                else:
                    pass
            except:
                pass
        # elif False not in map(lambda x:x in map(lambda x:chr(x),range(97,108)),list(address)):
        elif encoding == 'en':
            record = num_to_en_to_num(address)
        elif payload != 'None':
            record = payload

    except Exception, e:
        print '[!] Subdomain Invalid {}'.format(e)
    finally:
        return record


def num_to_en_to_num(address):
    """
    自定义简单的IP地址转换方式
    本程序自带了 将IP地址转换成十进制和16进制，一般WAF 都会识别到
    所以需要自己写一个自定义的地址转换方式

    传入的address是字符类型Ip地址,eg: '192.168.1.1'

    :param address:
    :return:
    """
    num_to_en = {}  # ip 转换成字母，比如'192.168.1.1' 转换成 'bjckbgikbkb'
    en_to_num = {}  # 字母转换成 ip ，比如'bjckbgikbkb' 转换成  '192.168.1.1'
    result = ''

    for k, v in enumerate(range(97, 108)):
        if k == 10:
            k = '.'
        num_to_en[str(k)] = chr(v)
        en_to_num[chr(v)] = str(k)

    try:
        if '.' in list(address):  # ip 编码成字母形式
            for i in list(address):
                result += num_to_en[i]
        else:  # 解码
            for i in list(address):
                result += en_to_num[i]
    except:
        print '[!] address error'

    return result


def ip_list_build(address):
    """
     批量生成各种编码形式的Ip
     en 编码：
    bjckbgikbkcei.nihao.com
    bjckbgikbkcej.nihao.com
    bjckbgikbkcfa.nihao.com
    bjckbgikbkcfb.nihao.com
    bjckbgikbkcfc.nihao.com
    bjckbgikbkcfd.nihao.com
    bjckbgikbkcfe.nihao.com

    int 编码：
    3232236024.nihao.com
    3232236025.nihao.com
    3232236026.nihao.com
    3232236027.nihao.com
    3232236028.nihao.com
    3232236029.nihao.com
    3232236030.nihao.com

    不编码:
    192.168.1.240.nihao.com
    192.168.1.241.nihao.com
    192.168.1.242.nihao.com
    192.168.1.243.nihao.com
    192.168.1.244.nihao.com
    192.168.1.245.nihao.com
    192.168.1.246.nihao.com
    192.168.1.247.nihao.com
    192.168.1.248.nihao.com

    :param address:
    :return:
    """
    print '1. Single IP Covert For En\n2. Build IP List'
    opt_req = raw_input("[+] [1 By Default/2]") or '1'
    if opt_req == '1':
        print num_to_en_to_num(address)
        exit()
    conf_main = conf_read('maindomain')[:-1]
    seg_len = raw_input("[+] Please Input Segment Length [24 By Default]") or 24  # 子网掩码
    encode_req = raw_input("[+] Please Input Encoding ['ipv4' By Default]")  # 编码方式，默认不编码
    mainDomain = raw_input("[+] Please Input Server Root Address [{} By Default]".format(conf_main)) or conf_main  # 域名
    segment = eval("ipaddr.IPv4Network('{}/{}').iterhosts()".format(address, int(seg_len)))  # 所有主机ip

    save_file = "{}_{}_{}.txt".format(time.strftime("%Y%m%d%X", time.localtime()).replace(':', ''),
                                      mainDomain.replace('.', '_'), (encode_req if encode_req else 'ipv4'))
    results = []

    try:

        if encode_req == '':
            results += ["{}.{}".format(str(i), mainDomain) + '\n' for i in list(segment)]
        elif encode_req == 'en':
            results += ["{}.{}".format(num_to_en_to_num(str(i)), mainDomain) + '\n' for i in list(segment)]
        elif encode_req == 'int':
            results += ["{}.{}".format(int(ipaddr.IPAddress(str(i))), mainDomain) + '\n' for i in list(segment)]
        elif encode_req == 'hex':
            results += ["{}.{}".format(str(i).encode('hex'), mainDomain) + '\n' for i in list(segment)]
        else:
            pass

        with open(save_file, 'w') as fd:
            fd.writelines(results)
        print '[+] Stored in the {}'.format(save_file)
    except Exception, e:
        exit(e.message)


def server_output(*args):
    client_ip = args[0][0]
    client_port = args[0][1]
    req_address = args[1]
    flag = "[{}] {}:{} => {} => {}".format(time.strftime("%X", time.localtime()), client_ip, client_port,
                                           conf_read('record_type'), req_address)

    return flag


def conf_read(*args):
    config = ConfigParser.ConfigParser()
    with open('lib/config.conf', 'r') as fd:
        config.readfp(fd)
        if args:
            return config.get('base', args[0])
        else:
            return config


def conf_set(options):
    config = conf_read()

    if '__class__' in dir(options):
        for k, v in options.items():
            config.set('base', k, v)
    else:
        config.set('base', 'record_type', options.record_type)
        config.set('base', 'payload', options.payload.__str__())
        config.set('base', 'encoding', options.encoding)
        config.set('base', 'rebinding', options.rebinding.__str__())

    if config.get('base', 'maindomain')[-1:] != '.':
        config.set('base', 'maindomain', config.get('base', 'maindomain') + '.')
    with open('lib/config.conf', 'w+') as fd:
        config.write(fd)


if __name__ == '__main__':
    ip_list_build('192.168.1.1')
