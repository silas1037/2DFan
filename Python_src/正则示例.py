#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re

# os.system("c:\\sam.bat")


import subprocess
#os.system("D: && cd D:\\11111118 && echo 114>1.txt && echo 214>>1.txt ")
#nowpath = "cd D:\\1104"
#os.system("D: && "+nowpath+" && pall.bat && fall.bat")

# !/usr/bin/env python 2

# coding : utf-8 3
import hashlib
from hashlib import md5
import time
import os


input_path = "D:/tst0002/新建文件夹 (3)"

standardlen = len(input_path)+1

def dirlist(path, allfile):
    filelist = os.listdir(path)
    for filename in filelist: #广义
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        elif filepath.endswith('bat'):
            allfile.append(filepath)
            with open(filepath,"r+", encoding='utf-8') as f:
                with open("D:/tst0002/1.txt", "a", encoding='utf-8') as fa:
                      lines = f.readlines()
                      for i in lines:
                          title = r'.*?"(.*)'
                          img1 = re.compile(title)
                          # html1 = i.decode('utf-8')  # python3
                          imglist1 = re.findall(img1, i)
                          print('BaiduPCS-Go d "'+str(imglist1)[2:-2])
                          fa.write('BaiduPCS-Go d "'+str(imglist1)[2:-2]+'\n')
    return allfile

a = dirlist(input_path,[])

# os.system("BaiduPCS-Go ru -length=34882652 -md5=95575cc59d93b844fff5e02f6c970858 \"算法导论中文版+算法导论中文版.pdf\"")

