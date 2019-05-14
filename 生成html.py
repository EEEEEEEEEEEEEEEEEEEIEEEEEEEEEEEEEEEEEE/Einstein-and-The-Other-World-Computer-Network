import os
import sys

sys.path.append('d:/librian')

import 導出文件

讀 = 導出文件.虛讀者('./劇本/試寫.liber', 簡化字=True)

html = f'''
<html>
    <head>
        <meta charset="utf8"/>
        <link rel="stylesheet" href="./劇本/css/紙樣式.css"/>
        <link rel="stylesheet" href="./劇本/css/樣式_人物名.css"/>
    <head>
    <body>
        <h1>爱因斯坦与异世界计算机网络</h1>
        {讀.body內容()}
    </body>
</html>
'''

with open('./index.html','w',encoding='utf8') as f:
    f.write(html)

import 字體縮減
