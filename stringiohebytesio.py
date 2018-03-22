#在内存中读写str
from io import StringIO


#先创建一个StringIO,再正常写入
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
#用getvalue()获取写入后的str
print(f.getvalue())

# 直接用read方法去读取，是没有值的
print('直接读',f.read())

#要用read来像读文件一样读取，可以用以下方法，用一个str初始化
f = StringIO('Hello!\nHi!\nGoodbye!') #在StringIO()里初始化
while True:
	s=f.readline()
	if s == '':
		break
	print(s.strip())
	
	
#要操作二进制数据，要用BytesIO
from io import BytesIO

#创建一个BytesIO，写入一些bytes
f = BytesIO()
f.write('中文'.encode('utf-8'))

# 直接读取写入的，无法读取到
print('当前游标地址：',f.tell())
# 设置游标地址为0
f.seek(0)
#再获取
print('设置游标到0后：',f.read())


#和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')	#初始化
print(f.read())


#补充解惑
'''
是因为the stream position的原因，当你用：

d = StringIO('Hello World')
其stream position为0（可以通过d.tell()获得），而后执行

d.readline()
stream position移动到11.因此在执行此方法时，返回的是空字符串。

类似的，使用

f = StringIO()
stream position也为0，而执行

f.write('Hello World')
stream position就移动到11了，因此你再执行readline时返回的依旧是空字符串，若你需要返回'Hello World'可以通过

f.seek(0)
调整stream position即可。

'''