#-*-coding:utf-8-*-
'''
Created on 2013年9月6日

@author: wangzining
'''
import urllib
import urllib2
url = 'http://p.nju.edu.cn'
values = {'username':'mf332070','password':'19910213wzn'}
data = urllib.urlencode(values)
# print data
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page