from urllib import request
import urllib

#直接爬取网页源码
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding=  'utf8')
urllib.response = request.urlopen('http://www.baidu.com', data=data)
#print(urllib.response.read().decode('utf-8'))

