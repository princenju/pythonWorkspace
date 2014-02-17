# -*- coding:utf-8 -*-
'''
Created on 2013.9.3

@author: wangzining
'''
import urllib2
import cookielib
import urllib
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://t.sohu.com/settings/bindMobile/registSendVerificationCode')
data={'mobileNumber':'13260717602'}
r=opener.open('http://t.sohu.com/settings/bindMobile/registSendVerificationCode',urllib.urlencode(data))
print r.read()
