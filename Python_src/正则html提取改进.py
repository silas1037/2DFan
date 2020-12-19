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

    for filename in filelist: #广义
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)

        elif filepath.endswith('html'):
            if 'index' in filepath:
                filepath = "file:///"+filepath.replace("\\","/")
                allfile.append(filepath)
    return allfile

filelist = dirlist("H:/eiiku/www.mygalgame.com-9b2c1648ee32360d0a6549baf570e88e35bad46f/www.mygalgame.com-9b2c1648ee32360d0a6549baf570e88e35bad46f", [])

for everyone in filelist:
    print(everyone)
    

for url in filelist:
    content = urllib.request.urlopen(url).read()

    title = r'<title> (.*?)\| 我的Galgame资源发布站</title>'
    img1 = re.compile(title)
    html1 = content.decode('utf-8')  # python3
    imglist1 = re.findall(img1, html1)
    for i in imglist1:
        print(i)

    #提取密码：<span style="color: #ff0000;">A553</span></span>
    title2 = r'<span style="color: #ff0000;">(\w{4})</span></span>'
    img2 = re.compile(title2)
    html2 = content.decode('utf-8')  # python3
    imglist2 = re.findall(img2, html2)
    for i in imglist2:
        print(i)

    reg = r'MD5: (\w{32})<' #括号里面就是匹配结果
    img = re.compile(reg)
    html = content.decode('utf-8')  # python3
    imglist = re.findall(img, html)
    for i in imglist:
        print(i)
    print("")