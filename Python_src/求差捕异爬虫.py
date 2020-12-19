

import os
import re
import urllib
import urllib.request
import time

'''
找出2dfan尚未下载的网页名，请求下载网页，处理404异常
'''

def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:  # 广义
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)

        elif filepath.endswith('html'):
            #if 'index' in filepath:
                filepath = "file:///" + filepath.replace("\\", "/")
                allfile.append(filepath)
    return allfile

filelist = dirlist("D:\\Gal\\2dfan",[])

Becut=[]

for i in filelist:
    Becut.append(i.split("/")[-1].split(".")[0])

nlist = range(1,9521)

result=[]

for i in nlist:
    if str(i) not in Becut and i > 8838:
        result.append(i)
        print(i)

print(str(len(result))+"\n-------------------------\n")


def getHtml(url):
    try:
        a = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e)  # 返回空值，中断程序，或者执行另一个方案
        return None
    else:
        a = urllib.request.urlopen(url)
        html = a.read()
        return html



def saveHtml(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    with open(file_name, "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)

savepath = "D:/Gal/Pythonwebgrab/"


'''
aurl = "https://www.2dfan.com/topics/1"
html = getHtml(aurl)
saveHtml(savepath + aurl.split("/")[-1], html)
'''
for i in result:
    aurl = "https://www.2dfan.com/topics/"+str(i)
    html = getHtml(aurl)
    if html != None:
        saveHtml(savepath + aurl.split("/")[-1] + ".html", html)
        print(str(i)+"下载成功")
    else:
        print(str(i)+"不存在网页")
    time.sleep(0.02) #避免too many request 429



#html = urllib.request.urlopen("https://www.2dfan.com/topics/9516")
'''try: html =  urllib.request.urlopen("https://www.2dfan.com/topics/9516")
except urllib.error.HTTPError as e:
    print(e) ''' # 返回空值，中断程序，或者执行另一个方案
#else: # 程序继续。

