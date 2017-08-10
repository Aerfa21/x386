# -*- coding: cp936 -*-

import re
import os
import os.path


def searchNTFS(catalog):
    """
     搜索所有ntfs ads文件目录，返回list
    :param catalog:
    :return:
    """
    resultL = []
    for root, dirs, files in os.walk(catalog):
        line = ''
        command = 'cd ' + root + '&' + 'dir /r'
        r = os.popen(command)
        info = r.readlines()
        for l in info:
            line = line + l
        reN = '\s(\S+)\:\$DATA'
        res = re.findall(reN, line)
        for re1 in res:
            if re1 != '':
                result = root + '\\' + re1
                resultL.append(result)
    return resultL


def searchInclude(catalog):
    """
    搜索所有包含ADS流的php文件
    :param catalog:
    :return:
    """
    reN = 'include\s*\("\S+\:\$DATA"\)'
    resultD = {}
    for root, dirs, files in os.walk(catalog):
        for f in files:
            dir = os.path.join(root, f)
            if dir[-4:] == '.php':
                try:
                    fp = open(dir, 'r')
                    for line in fp.readlines():
                        res = re.findall(reN, line)
                        for re1 in res:
                            if re1 != '':
                                result = re1
                                resultD[result] = root + '\\' + f
                except:
                    print "File :" + dir + " can't be read"
    return resultD


if __name__ == "__main__":

    reN = searchNTFS(os.getcwd())

    if reN:
        print "Suspicious ADS files Found"
        for _ in reN:
            print _

    reD = searchInclude(os.getcwd())

    if reD:
        print ""
        print "Suspicious Include ADS files Found"
        for key, value in reD.items():
            print key, "\t", value

