[![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://github.com/ForrestX386/x386/blob/master/BurpSuite-Extensions/COPYING) [![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/huaihuaiStyleIT)


�ο� Tr3jer ��ţ(https://github.com/Tr3jer/dnsAutoRebinding) ��ʵ�֣�����һ���޸ģ��޸���һЩСBUG��type ��record_type�������⣬���������ļ���д���⣬������룬�Ҷ�����ע�ͣ�

<br />
#### 0x00. ����ʽ����ʹ��������ߵ�ǰ��

1) ��������Ҫһ��DNS�����������������DNS�����������б�����

2����������Ҫע��һ������������ע�����������ý�NS��¼ָ�����DNS������

3) �޸�lib/config.conf �е�maindomain Ϊ��ע�������(������������.)


<br />
#### 0x01 ������Ĺ���

1��dns rebinding

��������ʲô�� dns rebinding����ο� [��ͤ�Ƽ���ţ������](https://ricterz.me/posts/Use%20DNS%20Rebinding%20to%20Bypass%20IP%20Restriction)

ԭ��Tr3jer��ţʵ�ֵ�ʱ��ֻ����������ʽΪ ip.maindomain ��ʽ����Ȼ���ip������10������ʽ����16������ʽ�����Զ�����루��Ȼ����Զ�����뱾dns������������ʶ��ģ�

���� 

ping 123.123.123.123.example.com 

��һ�η��� 123.123.123.123 

������һ��ping 123.123.123.123.example.com �ͷ��������õ�rebinding��IP��ַ

�����ping www.example.com �ͻ᷵�ش������޸ĵľ����һᲶ���������Ȼ�󷵻�һ��Ԥ�����õ�ip������8.8.8.8


2��dns ��¼����Ⱦ

���Ƕ�֪��վ��֮�ҹ��������ṩ���Բ�ѯ������CNAME��¼��MX��¼����ʵԭ����Ǻ�̨��ѯ ������CNAME��¼����MX��¼��Ȼ�󷵻ظ�ǰ��ҳ����Ⱦ�����Ǻ��û�й���CNAME�ķ���ֵ��ֱ�Ӷ���ǰ��
�����ͻᵼ������XSS��֮��Ĺ���

Tr3jer ��˵��0day �������


3������������ǰ׺���и��ֱ���


    ǰ׺��ʵ����IP��ַ����dns������ȡ���ǰ׺�������IP����Ϊdns����������ظ��ͻ���

    en ���룺
	
    bjckbgikbkcei.nihao.com
    bjckbgikbkcej.nihao.com
    bjckbgikbkcfa.nihao.com
    bjckbgikbkcfb.nihao.com
    bjckbgikbkcfc.nihao.com
    bjckbgikbkcfd.nihao.com
    bjckbgikbkcfe.nihao.com

    int ���룺
	
    3232236024.nihao.com
    3232236025.nihao.com
    3232236026.nihao.com
    3232236027.nihao.com
    3232236028.nihao.com
    3232236029.nihao.com
    3232236030.nihao.com

    ������:
	
    192.168.1.240.nihao.com
    192.168.1.241.nihao.com
    192.168.1.242.nihao.com
    192.168.1.243.nihao.com
    192.168.1.244.nihao.com
    192.168.1.245.nihao.com
    192.168.1.246.nihao.com
    192.168.1.247.nihao.com
    192.168.1.248.nihao.com
	
	
	
<br />

#### 0x02. �������ͼ

������֧��python2.x ���ݲ�֧��python3.x

������������������ķǱ�׼��

ipaddr

dnslib

���б�����ǰ��Ҫ���Ȱ�װ


��û�й�����������ֱ��ģ����һ�£����Ի������£�

dns �������� 10.1.100.3 ��kali2

dns �ͻ��ˣ�  10.1.100.1��windows7 ������dns ������ָ��10.1.100.3
	
	

