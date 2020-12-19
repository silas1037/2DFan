from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import *
import sqlite3

import os
import re
import urllib
import urllib.request


def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:  # 广义
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)

        elif filepath.endswith('html'):
            if 'index' in filepath:
                filepath = "file:///" + filepath.replace("\\", "/")
                allfile.append(filepath)
    return allfile



filepath = "D:/tst0002/Mirror/hosp.sql"
outpath = "D:/tst0002/Mirror/sam.txt"

with open(filepath, "r+", encoding='utf-8') as f:
    with open(outpath, "w", encoding='utf-8') as fp:
        lines = f.readlines()
        for i in lines:
            m = re.search(r'^D(.*?)$',i )
            #m = re.search(r'^INSERT(.*?)\((.*?)\;$',i )
            #m = re.search(r'^(\d{3,4}-)?(\d{7,8})$',i )
            print(m.group(0))
            print(m.group(1))
            '''
            word1 = r'VALUES \((.*?),(.*?)\)' #VALUES (
            style1 = re.compile(word1)
            # html1 = i.decode('utf-8')  # python3
            imglist1 = re.findall(style1, i) #查找

            print(str(imglist1))
            fp.write(str(imglist1)+ '\n')
            '''

m = re.search(r'^(\d{3,4}-)?(\d{7,8})$', '020-82228888')
print(m.group(0))
print(m.group(1))
print(m.group(2))