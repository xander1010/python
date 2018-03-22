#def add(x,y,f):
#	return f(x)+f(y)

#print(add(-5,8,abs))

#def f(x):
#	return x * x

#r = map(f,[1,2,3,4,5,6,7,8,9])
#print(list(r))

#L = []
#for i in range(1,10):
#	L.append(i*i)
#print(L)

from functools import reduce
#def fn(x,y):
#	return x*10+y

#print(reduce(fn,[1,2,3,4,5,6]))

#def char2int(s):
#	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

#print(reduce(fn,map(char2int,'465616')))

#简化一下：

def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2int(s):
		#通过map方法遍历每一个字符来取得对应的值并生成迭代器
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	#reduce方法引用fn两个参数来对map出的迭代器转化成Int
	return reduce(fn,map(char2int,s))

print(str2int('45466545'))


#练习：
#编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
	def ji(m,n):
		return m * n
	return reduce(ji,L)

print('3 * 5 * 7 * 9 =',prod([3,5,7,9]))

#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字

def normalize(name):
    return name.lower().capitalize()

L1 = ['AdaM', 'LisA', 'BaRt']
L2 = list(map(normalize, L1))
print(L2)


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(L):
    def fn(x,y):
        return x*10+y
    def fn2(x,y):
        return (x*0.1+y)
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    L1=L.split('.')
    LL=reduce(fn,map(char2num,L1[0]))
    test1=L1[1][::-1]+'0'
    LR=reduce(fn2,map(char2num,test1))
    return  LL+LR

print(str2float('123.123'))

print('####################分隔符#########################')

#filter：根据返回值是true还是false决定保留还是丢弃元素
#用法:filter(f,[1,2])，主要是函数要为筛选的，相当于让数列数据显示出来的条件
def is_odd(n):
	return n % 2 ==1
li=[1, 2, 4, 5, 6, 9, 10, 15]
print(list(filter(is_odd,li)))	
	
def notempty(ss):
	return ss and ss.strip() #strip()为空去除所有空和空格，若指定去除字符则为去除首与尾对应的字符
print(list(filter(notempty,['A', '', 'B', None, 'C', '   '])))

print('####################分隔符#########################')
#sorted函数：排序算法，sorted([2,1,3]),sorted([2,1,-3],key=abs)
print(sorted([2,6,4,964,-4165,-1,3,4],key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#按字母排序，不考虑大小定，转换为同样的再比较
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower,reverse=True))

#练习：
#用sorted()对列表分别按名字排序
#列表里一个元素里还有多个元素，要按其中一个来排序，所以要定义Key函数取其中某个
def byname(t):
	print(t[0])
	return t[0]
	

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L,key=byname))

def byscore(t):
	return t[1]
print(sorted(L,key=byscore,reverse=True))
print(L[1])





