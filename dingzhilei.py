class Student(object):
	def __init__(self,name):
		self.name = name
	#是为了用户看到的字符，在用户端显示用
	def __str__(self):
		return 'Student object (name: %s)'%self.name
	#为了直接输出实例 a显示友好时用以下方法，面向开发
	__repr__ = __str__
	
	#调用的属性不存在时到这里找，这里没有的默认返回None
	def __getattr__(self,attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda:25
		raise AttributeError('\'Student\' object has no %s'%attr)

	def __call__(self):
		print('My name is %s' %self.name)
#实例化对象a		
a = Student('lily')	

#>>>a #直接输出实例a ，没有__repr__()方法时显示为<__main__.Student object at 0x109afb310>

print(a)
print(Student('mike'))

#__iter__用法，用于要让类用于for .. in 循环时
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1
	
	def __iter__(self):
		return self
		
	def __next__(self):
		self.a,self.b = self.b , self.a + self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a
		
for n in Fib():
	print(n)

# __getitem__ , 需要像list那样按照下标取出元素时
class Fibo(object):
	def __getitem__(self,n):
		#判断输入的是int
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a + b
			return a
		#判断输入的是切片
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L=[]
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L

#实例化对象			
f = Fibo()
#输入的是int
print(f[5])

#普通列表直接加切片打印出来
print(list(range(100))[5:10])

# 输入的是切片，在类里的方法要加判断
print(f[0:5])

#没有对setup做处理
print(f[0:5:2])

# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素

#__getattr__ ，可以用这个方法来加属性
#依据第一个类来举例子
print(a.score)
print(a.age())
# print(a.aaa)

# 要写SDK，给每个URL对应的API都写一个方法，那得累死，
# 而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用
class Chain(object):
	
	def __init__(self,path=''):
		self._path = path
	
	def __getattr__(self,path):
		return Chain('%s/%s' %(self._path,path))
	
	def __str__(self):
		return self._path
		
	__repr__ = __str__
		

print(Chain().status.user.timeline.list)


# __call__ ，在类中添加此方法可让实例本身上调用方法
#以第一个类为例来举例

#直接在实例后加（）调用 __call__
a()

# 用callable()函数，可以判断对象是否为“可调用”对象
print(callable(Student),callable(max),callable('str'))





		