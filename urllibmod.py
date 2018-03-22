'''
from urllib import request

对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650
进行抓取，并返回响应

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:',f.status,f.reason)
	for k,v in f.getheaders():
		print('%s: %s' %(k,v))
	print('Data:',data.decode('utf-8'))
'''	

# 模拟浏览器发送GET请求，就需要使用Request对象，
# 通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
# 例如，模拟iPhone 6去请求豆瓣首页
'''
from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent','Mozilla/6.0(iphone; CPU iphone OS 8_0 like Mac OS X) AppleWebKit/536.26(KHTML,like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	print('Status:',f.status,f.reason)
	for k , v in f.getheaders():
		print('%s:%s'%(k,v))
	print('Data:',f.read().decode('utf-8'))
'''


# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。

# 我们模拟一个微博登录，先读取登录的邮箱和口令，
# 然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入
from urllib import request,parse

print('login to weibo.cn...')
email = input('Email:')
passwd = input('Password:')
login_data = parse.urlencode([
	('username',email),
	('password',passwd),
	('entry','mweibo'),
	('client_id',''),
	('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,data = login_data.encode('utf-8')) as f:
	print('Status:',f.status,f.reason)
	for k,v in f.getheaders():
		print('%s:%s'%(k,v))
	print('Data:',f.read().decode('utf-8'))
	
# Handler

# 如果还需要更复杂的控制，比如通过一个Proxy(代理)去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
'''
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
'''	

'''	
小结

urllib提供的功能就是利用程序去执行各种HTTP请求。
如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。
伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，
User-Agent头就是用来标识浏览器的
'''

print('++++++++++++++++++++下面是练习++++++++++++++++++++++')
# 练习:

# 利用urllib读取JSON，然后将JSON解析为Python对象：
from urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        try:
            return json.loads(f.read().decode("utf-8"))
        except ValueError:
            print("ValueError:", url)


# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')








