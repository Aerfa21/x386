
rem ������Ҫ��װ��java��python��androidStudio


::��python����PATH��
@echo off
echo python����PATH��
wmic ENVIRONMENT where "name='path' and username='<system>'" set VariableValue="%path%;C:\Python27;C:\Python27\Scripts"



rem ��ӻ�������JAVA_HOME
echo ��ӻ�������JAVA_HOME
set regpath=HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
set evname=JAVA_HOME
set javapath=C:\Program Files\Java\jdk1.8.0_121
reg add "%regpath%" /v %evname% /t reg_sz /d "%javapath%" /f

echo java����PATH��
wmic ENVIRONMENT where "name='path' and username='<system>'" set VariableValue="%path%;%JAVA_HOME%\bin;%JAVA_HOME\jre\bin%"

rem ��ӻ�������CLASS_PATH
set evname=CLASS_PATH
set value=".;%JAVA_HOME%\lib\tools.jar;%JAVA_HOME%\lib\dt.jar; "
reg add "%regpath%" /v %evname% /t reg_expand_sz /d %value% /f



rem ��ӻ�������ANDROID_SDK_HOME

set regpath=HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
set evname=ANDROID_SDK_HOME
set value=D:\sdk
reg add "%regpath%" /v %evname% /t reg_sz /d "%value%" /f

echo ANDROID_SDK_HOME��ִ���ļ�����PATH��
wmic ENVIRONMENT where "name='path' and username='<system>'" set VariableValue="%path%;%ANDROID_SDK_HOME%\tools;%ANDROID_SDK_HOME\platform-tools;%"



rem �Զ���װȱʧpy module
echo �Զ���װȱʧpy module
pip install -U pip
pip install ujson
pip install requests
pip install bs4
pip install django
pip install jinja
pip install flask
pip install xlwt
pip install lxml 
pip install ipaddress
pip install ipaddr
pip install prettytable
pip install setuptools
pip install wheel
pip install netiaces
pip install pyreadline
pip install sh
pip install selenium
pip install urllib3
pip install ipdb
pip install scrapy
pip install redis
pip install paramiko
pip install pymongo
pip install virtualenv
pip install gevent
pip install sphinx
pip install pymongo
pip install colorama
pip install termcolor
pip install netaddr
pip install pydns
pip install libnamp 
pip install impacket
pip install colorlog
pip install pypcap
pip install PySocks
pip install tornado
pip install redis
pause