# 2DFan
2dfan介绍攻略感想帖子抓取整合

格式：https://www.2dfan.com/topics/xxxx
下载全部html（9千多条）

其中有些网页为404，做好异常捕获处理

使用更换IP方法以及延时做好Too Many Request处理

下载完所有网页后，集中于文件夹中做正则处理。

标题捕获：`r'<title>(.*?)</title>'`
帖子内容捕获：`r'"topic-content">([\s\S]*?)</div'`

捕获完之后处理混入的标签如`<br />`。

写入“序号-标题”的txt文本即可。
