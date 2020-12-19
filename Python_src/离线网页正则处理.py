
import os
import re
import urllib
import urllib.request
import time

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

def zze(ball,url):
    content = urllib.request.urlopen(url).read()
    img = re.compile(ball)
    html = content.decode('utf-8')  # python3
    catchlist = re.findall(img, html)
    return catchlist

filelist = dirlist("D:/Gal/2dfan",[])

def Htmlrep(s):
    s = s.replace("&amp", "&")
    s = s.replace("&quot", "“")
    s = s.replace("&lt", "<")
    s = s.replace("&gt", ">")
    s = s.replace("&nbsp", " ")
    s = s.replace("&laquo", "«")
    s = s.replace("&raquo", "»")
    s = s.replace("&lsquo", "‘")
    s = s.replace("&rsquo", "’")
    s = s.replace("&ldquo", "“")
    s = s.replace("&rdquo", "”")
    s = s.replace("&sect", "§")
    s = s.replace("&copy", "©")
    s = s.replace("&hellip", "…")
    s = s.replace("&oplus", "⊕")
    s = s.replace("&nabla", "∇")
    s = s.replace("&times", "×")
    s = s.replace("&divide", "÷")
    s = s.replace("&plusmn", "±")
    s = s.replace("&radic", "√")
    s = s.replace("&infin", "∞")
    s = s.replace("&ang", "∠")
    s = s.replace("&int", "∫")
    s = s.replace("&deg", "°")
    s = s.replace("&ne", "≠")
    s = s.replace("&equiv", "≡")
    s = s.replace("&le", "≤")
    s = s.replace("&ge", "≥")
    s = s.replace("&perp", "⊥")
    s = s.replace("&there4", "∴")
    s = s.replace("&pi", "π")
    s = s.replace("&sup1", "¹")
    s = s.replace("&sup2", "²")
    s = s.replace("&sup3", "³")
    s = s.replace("&crarr", "↵")
    s = s.replace("&larr", "←")
    s = s.replace("&uarr", "↑")
    s = s.replace("&rarr", "→")
    s = s.replace("&darr", "↓")
    s = s.replace("&lArr", "⇐")
    s = s.replace("&uArr", "⇑")
    s = s.replace("&rArr", "⇒")
    s = s.replace("&dArr", "⇓")
    s = s.replace("&alpha", "α")
    s = s.replace("&beta", "β")
    s = s.replace("&gamma", "γ")
    s = s.replace("&Delta", "Δ")
    s = s.replace("&theta", "θ")
    s = s.replace("&lambda", "λ")
    s = s.replace("&Sigma", "Σ")
    s = s.replace("&tau", "τ")
    s = s.replace("&omega", "ω")
    s = s.replace("&Omega", "Ω")
    s = s.replace("&bull", "•")
    return s


outpath = "D:/Gal/2dfantout/"

for url in filelist:

    outfile = url.split("/")[-1].replace(".html",".txt")

    #with open(outfile, "w", encoding='utf-8') as fp:
    ball = r'<title>(.*?)</title>'
    imglist = zze(ball,url)
    for i in imglist:
        i = i.replace("_2DFan", "")
        #print(i)
        #print("\n##########\n")
        outfile = outfile.replace(".txt","-" + i + ".txt")
        outfile = outfile.replace("/","-")
        outfile = outfile.replace("\\","-")
        outfile = outfile.replace(":","：")
        outfile = outfile.replace("*","-")
        outfile = outfile.replace("?","？")
        outfile = outfile.replace("\"","")
        outfile = outfile.replace("<","《")
        outfile = outfile.replace(">","》")
        outfile = outfile.replace("|","-")
        outfile = outpath + outfile
        with open(outfile, "w", encoding='utf-8') as fp:
            fp.write(i+"\n")

    ball = r'"topic-content">([\s\S]*?)</div'
    imglist = zze(ball, url)
    for i in imglist:
        i = i.replace("<br />","")
        i = i.replace("<P>","")
        i = i.replace("<p>","")
        i = i.replace("</P>","")
        i = i.replace("</p>","")
        i = i.replace("<h4>","")
        i = i.replace("</h4>","")
        i = Htmlrep(i)
        #print(i)
        #print("\n##########\n")
        with open(outfile, "w", encoding='utf-8') as fp:
            fp.write(i+"\n")
    fp.close()
