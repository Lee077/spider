# coding=utf-8
import cookielib
import urllib2

url = 'http://www.baidu.com'
filename = "cookie.txt"

# LWPCookieJar是创建文件格式兼容的FileCookieJar实例
# FileCookieJar实例是检索cookie信息并存储文件中。
# 参数delayload为True时支持延迟访问文件，需要时读取文件或存储数据
cookie = cookielib.LWPCookieJar(filename)

# 创建cookie处理器   handler指处理程序
handler = urllib2.HTTPCookieProcessor(cookie)

# 通过handler创建opener
opener = urllib2.build_opener(handler)

# 创建全局opener
urllib2.install_opener(opener)

# 创建请求
response = opener.open(url)

# 保存cookie到文件中
cookie.save(ignore_discard=True,ignore_expires=True)