@echo off

rem windows2003 ����3389
rem ǰ����Windows Management Instrumentation��Winmgmt����������������

wmic path win32_terminalservicesetting where (__CLASS != "") call setallowtsconnections 1