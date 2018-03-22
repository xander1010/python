print(type(123))

import types

def fn():
	pass

# 通过导入types模块，可以看到对应对象的类型，是不是函数	
print(type(fn) == types.FunctionType,

type(abs) == types.BuiltinFunctionType,

type(lambda x:x)== types.LambdaType,

type((x for x in range(10)))== types.GeneratorType)


# 用isinstance来判断对象类型,isinstance(数据,要判断的类型)
#可以判断一个对象是不是属于某个类
print(isinstance(123,int))

#基本类型也可以用isinstance()判断
isinstance('a', str)
# True
isinstance(123, int)
# True
isinstance(b'a', bytes)
# True

# 可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
isinstance([1, 2, 3], (list, tuple))
# True
isinstance((1, 2, 3), (list, tuple))
# True

#获得一个对象的所有属性和方法，可以使用dir()函数
print(dir('AB'))

#调用len()相当于'aaa'自动调用本身的__len__()方法
print(len('aaa'),'aaa'.__len__()) #是一样的

#类可以自己写一个__len__方法，就可以调用了
class Dog(object):
	def __len__(self):
		return 100
# 实例化一个对象
dog = Dog()

print(dog.__len__(),len(dog))

#转换成小写字母
print('ABC'.lower())
#首字母大写
print('JACKLOVE'.capitalize()) 

#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class Myobject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

d = Myobject()
print(d.power())

# 有属性'x'吗？并获取值
print(hasattr(d,'x'),d.x)

# 有属性'y'吗？
print(hasattr(d,'y'))

# 设置一个属性'y'
setattr(d,'y',19)

# 有属性'y'吗？ 并获取值
print(hasattr(d,'y'),d.y)

#获取一个属性的值
print(getattr(d,'y'))


#也可以用来判断是否有方法
print(hasattr(d,'power'))

#获取已有的方法
print(getattr(d,'power'))

#将获取的方法指定给一个对象
fn = getattr(d,'power')

print(fn())