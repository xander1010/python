# 普通函数定义，出错了要一个一个去找
# def foo():
	# r = some_function()
	# if r ==(-1):
		# return (-1)
	# do something
	# return r
	
# def bar():
	# r = foo()
	# if r == (-1):
		# print('Error')
	# else:
		# pass

#在认为某些代码会出错时，可以用try来运行		
try:
	print('try...')
	r = 10 / int('2')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
#可以设置多个错误类型捕获
except ZeroDivisionError as e:
	print('except:',e)
#可以在except后加else,没有错误时会运行
else:
	print('no error')
# 有finally时一定会运行
finally:
	print('finally...')
print('END')

print('*********分隔线*************')

#演示在合适层次使用try就可以了
def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s) * 2

#直接在要用到的，合适的层次捕获错误就可以了
def main():
	try:
		bar(0)
	#捕获异常
	except Exception as e:
		print('Error:',e)
	finally:
		print('finish')

# 调用main()函数		
main()	
	
print('*********分隔线*************')
#不加try，调用ma()
#在用logging时要先导入模块
import logging

def fo(a):
	return 10 / int(a)
	
def ba(a):
	return fo(a) * 2
def ma():
	try:
		ba('0')
	except Exception as e:
		#用logging模块记录错误信息，可以通过配置记录到日志文件
		logging.exception(e)
ma()
print('END')	
	
print('*********分隔线*************')
#自定义错误类
class FooError(ValueError):
	pass

def fo1(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value:%s'%s)
	return 10 / n

# fo1('0')

print('*********分隔线n-1*************')
#有raise时后面又有try
def fan(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value:%s'%s)
	return 10 / n
def ban():
	try:
		fan('0')
	except ValueError as e:
		print('ValueError')
		raise
		
# ban()


print('*********分隔线n*************')
#练习：运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
from functools import reduce

def str2num(s):
	try:
		return int(s)
	except ValueError as e:
		print('输入数字',e)
		return 1
	except Exception as e:
		print('换成浮点吧')
		return float(s)
	
		
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + a')
    print('99 + 88 + 7.6 =', r)

main()
	
	



