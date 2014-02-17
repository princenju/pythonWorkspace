# -*- coding:utf-8 -*-
'''
Created on 2013年9月3日

@author: wangzining
'''

import os,random
path="I:"
l=os.listdir(path)
result=[]
for name in l:
    if name.decode("gbk").encode("utf-8")=="电视剧" or name.decode("gbk").encode("utf-8")=="纪录片":
        d=path+"//"+name
        li=os.listdir(d)
        for lis in li:
            result=result+[d+"//"+lis]
r=random.randint(0,len(result)-1)
print r
start_directory = result[r].replace("//",'\\')
os.system("explorer.exe %s" % start_directory)
