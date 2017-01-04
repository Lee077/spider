#coding=utf-8
import urllib
import urllib2
import cookielib
# 实现cookie有cookielib模块，和HTTPCookieProcessor


url = 'http://www.baidu.com'
# 创建cookie实例对象，用于管理值，存储生成的cookie,给请求添加cookie对象
cookie = cookielib.CookieJar()

# 创建cookie处理器，handler是实例对象
handler =urllib2.HTTPCookieProcessor(cookie) 

# 创建opener，opener是实例对象
opener = urllib2.build_opener(handler)

# 将opener变成全局opener
urllib2.install_opener(opener)

# cookie变了,现在已经有完整cookie
response = opener.open(url)

# 按照格式存储cookie
cookies = ""
for item in cookie:
	cookies = cookies + item.name + '=' + item.value + ';'
print cookies[:-1]