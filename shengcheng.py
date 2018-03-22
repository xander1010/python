#g = (x * x for x in range(10))
#for n in g:
#	print(n)

#斐波拉契数列用generator
def fib(max):
	n,a,b =0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n + 1
	return 'done'

g = fib(-1)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('values is:',e.value)
		break

#测试yield用法，用Next()执行		
#def ce(i):
#	while i >= 0 or i < 0 :
#		yield i
#		i = i + 1
#		if i==10:
#			break
#	return "done"
print('############################分隔符############################')

#杨辉三角
def yan(line):
	i,L = 0,[1]
	for n in range(line):
		print(L)
		L = [1] + [L[i]+L[i+1] for i in range(0,len(L)-1)] +[1]
	return 'over'

yan(5)
print('############################分隔符############################')

a=[1,1,3]
print(len(a))
b=[a[i]+a[i+1] for i in range(0,len(a)-1)]
print(b)

print('############################分隔符############################')

#生成器：
def yang(han):
	q,arr=0,[1]
	for s in range(han):
		yield (arr)
		arr = [1] + [arr[q]+arr[q+1] for q in range(0,len(arr)-1)] +[1]
	return 'over'
	
g = yang(13)
while True:
	try:
		x = next(g)
		print("g:",x)
	except StopIteration as e:
		print("value:",e.value)
		break

#看不懂的新方法。。
def triangles(n):
    L = [1]
    while len(L) < n:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
		
		
		