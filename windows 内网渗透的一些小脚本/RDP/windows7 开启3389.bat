@echo off

rem windows7 ����3389.bat
rem ǰ����Windows Management Instrumentation��Winmgmt����������������

wmic /namespace:\\root\cimv2\terminalservices path win32_terminalservicesetting where (__CLASS != "") call setallowtsconnections 1

wmic /namespace:\\root\cimv2\terminalservices path win32_tsgeneralsetting where (TerminalName ='RDP-Tcp') call setuserauthenticationrequired 1