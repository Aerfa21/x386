[![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://github.com/ForrestX386/x386/blob/master/BurpSuite-Extensions/COPYING) [![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/huaihuaiStyleIT)


参考 Tr3jer 大牛(https://github.com/Tr3jer/dnsAutoRebinding) 的实现，做了一点修改，修复了一些小BUG，做了实际测试（type 和record_type混用问题，还有配置文件读写问题，详见代码，代码中都做了注释）

<br />
#### 0x00. 在正式环境使用这个工具的前提

1) 首先你需要一个DNS解析服务器（在这个DNS服务器上运行本程序）

2）首先你需要注册一个域名，并在注册商那里配置将NS记录指向你的DNS服务器

3) 修改lib/config.conf 中的maindomain 为你注册的域名(别忘记最后面的.)


<br />
####. 0x01 本程序的功能

1）dns rebinding

如果不理解什么是 dns rebinding，请参考 [长亭科技大牛的文章](https://ricterz.me/posts/Use%20DNS%20Rebinding%20to%20Bypass%20IP%20Restriction)

原先Tr3jer大牛实现的时候，只允许域名形式为 ip.maindomain 形式，当然这个ip可以是10进制形式或者16进制形式或者自定义编码（当然这个自定义编码本dns服务器程序能识别的）

比如 

ping 123.123.123.123.example.com 

第一次返回 123.123.123.123 

再运行一次ping 123.123.123.123.example.com 就返回你配置的rebinding的IP地址

如果你ping www.example.com 就会返回错误，我修改的就是我会捕获这个错误，然后返回一次预先设置的ip，比如8.8.8.8


2）dns 记录的污染

我们都知道站长之家工具中有提供可以查询域名的CNAME记录和MX记录，其实原理就是后台查询 域名的CNAME记录或者MX记录，然后返回给前端页面渲染，但是后端没有过滤CNAME的返回值，直接丢给前端
这样就会导致类似XSS的之类的攻击

Tr3jer 所说的0day 就是这个


3）批量将域名前缀进行各种编码


    前缀其实就是IP地址，本dns程序会截取这个前缀，解码成IP，作为dns解析结果返回给客户端

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
	
	
	
<br />

####. 0x02. 测试与截图

本程序支持python2.x ，暂不支持python3.x

本程序依赖两个额外的非标准库

ipaddr

dnslib

运行本程序前需要事先安装


我没有购买域名，我直接模拟了一下，测试环境如下：

dns 服务器： 10.1.100.3 ，kali2

dns 客户端：  10.1.100.1，windows7 ，配置dns 服务器指向10.1.100.3
	
1. dns rebinding测试
	
1）启动DNS 服务器：

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/start1.png "")	

2）客户端开始ping （相当于DNS查询）

第一次查询，返回123.123.123.123

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/first.png "")	

第二次查询，返回rebinding 设置的ip（当然，这个IP一般设置为内部IP，dns rebinding技术就是为了绕过某些ssrf 防护的限制）

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/second.png "")	

前缀是www，不是ip形式

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/3.png "")	

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/4.png "")	

前缀是自定义编码 (-e 表示自定义编码，-e 可以单独用，但和-r 一起用比较符合实际场景)

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/rebind.png "")	

第一次查询：返回的是编码前缀的解码结果(bjckbgikbkcei 是192.168.1.248 自定义编码的后值，这个编码方式位于lib/common.py 中的num_to_en_to_num函数)

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/5.png "")	

第二次查询：返回的是renbinding设置的IP

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/6.png "")	


2. DNS 记录污染测试

支持CNAME 和MX 记录污染

1）CNAME 记录污染

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/7.png "")	

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/8.png "")	


2）MX 记录污染

![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/9.png "")	


![alt ""](https://raw.githubusercontent.com/ForrestX386/static/master/pic/security_dev/10.png "")	




