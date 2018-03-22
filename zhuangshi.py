import functools
#装饰器
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log("running")
def now():
	print('2017-11-24')

print(now())
print(now.__name__) #如果不加@functools.wraps(func)，这时的now名是wrapper

# print(now.__name__)
# print(f.__name__)

# def ce(x,y,*args):
	# print(x,y,*args)
# print(ce('a',13,123,'a'))

print("***************分隔符******************")

#简单的装饰器，相当于执行的是af=log1(af)
def log1(fun):
	@functools.wraps(fun)
	def war(*args,**kw):
		print('now is running %s()'%fun.__name__)
		return fun(*args,**kw)
	return war
@log1
def af(L=[]):
	L2=sorted(L)
	return L2
print(af([1,4,3,32,5,65]))


print("***************分隔符******************")

#练习：

def log(text):
    def decorator(func):
         def wrraper(*args,**kwargs):
             if(isinstance(text,str)):
              print('%s: call %s()' % (text, func.__name__))
             else:
               print('call %s()'%text.__name__)
             return func(*args,*kwargs)
         return wrraper
    return  decorator  if(isinstance(text,str)) else decorator(text)

# #要点：
# (isinstance(text,str))
# 若是加字符串的话返回函数名称：
# 调用执行为：log(text)(func)=>decorator(func)=>wrraper备用
# 若不是字符串的话直接执行decorator(text)其中text即func
# 调用执行为：log(func)(func)=>decorator(func)=>wrraper用,实只有log的时候就直接执行的decorator(func)

print("***************分隔符******************")
#这个包含了运行的具体时间和运行的时机：
from functools import wraps
from time import time, sleep

start_time = time()
print("\n现在开始运行...\n\n**********************\n")

def log(text):
    def decorator(func):
        @wraps(func)
        def wrapers(*args, **kw):
            print("运行{0}()，运行了 {1} 秒\n".format(func.__name__, time()-start_time))
            startTime =  time()
            return (func(*args, **kw),print("函数{0}()执行了 {1} 秒，结束\n".format(func.__name__, time()-startTime)))[0]
        return wrapers
    return (decorator,print("带参数的装饰器，参数为： '{}' ".format(text) ))[0] if text.__str__() == text else decorator(text)

@log
def abc():
    print("运行函数abc()，睡 5 秒\n")
    sleep(5)

@log('带参数\n')
def efg():
    print("运行函数efg(),睡 3 秒\n")
    sleep(3)    

abc()
efg()

print("运行结束，一共运行了",time()-start_time,"秒")
