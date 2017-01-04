#coding=utf-8
import urllib2
import cookielib
# 从文件中获取cookie并访问
# 读取cookie是用cookielib模块和HTTPCookieProcessor类

url = 'http://www.baidu.com'

# 创建LWPCookieJar实例对象
cookie = cookielib.LWPCookieJar()

# 读取文件中cookie到变量
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)

#通过cookie创建handler
handler = urllib2.HTTPCookieProcessor(cookie)

# 创建opener
opener = urllib2.build_opener(handler)

urllib2.install_opener(opener)

# 创建请求request
request = urllib2.Request(url)

response = opener.open(request)

html = response.read()

f = open('cookieRead.html','w')
f.write(html)
f.close



