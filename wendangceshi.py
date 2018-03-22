def abs(n):
	'''
	Function to get absolute value of number.
	
	Examp:
	
	>>> abs(1)
	1
	>>> abs(-1)
	1
	>>> abs(0)
	0
	'''
	return n if n>=0 else (-n)
	
#用doctest测试Dict
#两个地方可以放doctest测试用例，一个位置是模块的最开头，
#另一个位置是函数声明语句的下一行
class Dict(dict):
	#以下>>>后面有空格，Traceback和KeyError：后面空格也要加上
	'''
	Simple dict but also support access as x.y style.
	
	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2 = Dict(a=1,b=2,c='3')
	>>> d2.c
	'3'
	>>> d2['empty']
	Traceback (most recent call last):
		...
	KeyError: 'empty'
	>>> d2.empty
	Traceback (most recent call last):
		...
	AttributeError: 'Dict' object has no attribute 'empty'
	'''
	
	def __init__(self,**kw):
		super(Dict,self).__init__(**kw)
		
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'"%key)
			
	def __setattr__(self,key,value):
		self[key]=value

		
# if __name__=='__main__':
	# import doctest
	# 默认testmod()是verbose=false，为true时打印出来
	# doctest.testmod() 


#练习:	对函数fact(n)编写doctest并执行：
def fact(n):
	'''
	Calculate 1*2*...*n
	
	>>> fact(1)
	1
	>>> fact(10)
	3628800
	>>> fact(-1)
	Traceback (most recent call last):
		...
	ValueError
	'''
	
	if n<1:
		raise ValueError()
	if n==1:
		return 1
	return n*(fact(n-1))

# print(fact(-1))
	
if __name__=='__main__':
	import doctest
	doctest.testmod(verbose=True)
	
#使用doctest时会把对应地方'''...'''中的注释>>> 的代码尝试以shell方式运行来测试

	
	