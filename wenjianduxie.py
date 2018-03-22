try:
	f = open('E:/python/file/test.txt','r')
	print(f.read())
finally:
	if f:
		f.close()

#使用with语句可以更简洁，with自带清除对象的方法，如close()		
with open('./file/test.txt','r') as f:
	print(f.read())

#只读取10个字符	
with open('./file/test.txt','r') as f:
	print(f.read(10))	

#调用一次读取一行的内容	
with open('./file/test.txt','r') as f:
	print('read:',f.readline())
	print('read:',f.readline())	

#读取所有并按行返回list，可以用for .. in 来用	
with open('./file/test.txt','r') as f:
	print(f.readlines())	

try:
	f = open('E:/python/file/test.txt','r')

	for line in f.readlines():
		print(line.strip()) #用strip()去掉列表后面的\n
finally:
	if f: #判断文件如果为打开状态
		f.close()
		
#读取二进制文件，如图片，视频等，用'rb'模式打开		
with open('./file/pic.png','rb') as f:
	print('pic:',f.read())
		
#要读取非utf-8编码文件，要给open()函数传入encoding参数,读GBK就加GBK
with open('./file/test.txt','r',encoding='gbk') as f:
	print('GBK:',f.read())	
	
#open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理,ignore直接忽略	
with open('./file/test.txt','r',encoding='gbk',errors='ignore') as f:
	print('error:',f.read())	


#写文件，区别是调用open()函数时，
# 传入标识符'w'或者'wb'表示写文本文件或写二进制文件	
#用'a'代表在后面追加，还有其他的a+,w+,等

f = open('./file/test.txt','a')
f.write('123')
f.close

with open('./file/test.txt','a') as f:
	f.write('456')

with open('./file/test.txt','r') as f:
	print(f.read())






		
		