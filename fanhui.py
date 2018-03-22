# 一个简单的求和函数
def calcsum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

print(calcsum(1,2,3))

print('##################分隔栏########################')

# 求和返回函数
def lazysum(*args):
	def sum():
		ax = 0 
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazysum(1,2,4,5,6,3)
print(f())

print('##################分隔栏########################')
# 闭包例子这里fs=[f,f]
def count():
	fs = []
	for i in range(1,3):
		def f():
			return i * i
		fs.append(f)
	return fs

f1,f2 = count()
print(f1())

# 返回函数不要引用任何循环变量，或者后续会发生变化的变量
print('##################分隔栏########################')

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs
f1,f2,f3 = count()
#ff = count()
print(f1(),f2(),f3())


print('##################分隔栏########################')

def dizen():
	i = 0
	while True:
		yield i+1
	return i
def tiqu(t):
	ti = dizen()
	for d i range(t):
		
	
print(dizen())
	
#练习：
def createCounter():
    n = 0
    def counter():
        nonlocal n#从外面取到n并+1
        n += 1
        return n
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA(),counterA()) # 1 2 3 4 5 6

counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

