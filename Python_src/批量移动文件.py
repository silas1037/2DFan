
import os

def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:  # 广义
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)

        elif filepath.endswith('txt'):
            #if 'index' in filepath:
                #filepath = "file:///" + filepath.replace("\\", "/")
            allfile.append(filepath)
    return allfile

filelist = dirlist("D:/Gal/2dfantout",[])
for i in filelist:
    print(i)
    if "攻略" in i:
        print(i)
        os.system("move \""+ i+ "\" ./攻略")
