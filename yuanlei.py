class Hello(object):
	def hello(self,name = 'world!'):
		print('hello,%s'%name)


	
h = Hello()
h.hello
print(type(Hello))
print(type(h))

#用type()函数创建一个class对象

def fn(self,name = 'haha'):
	print('Hello,%s'%name)

#三个参数：class名，继承对象tuple写法，方法名与函数绑定	
Hello = type('Hello',(object,),dict(hello = fn))

hh = Hello()
hh.hello
print(type(Hello))
print(type(hh))