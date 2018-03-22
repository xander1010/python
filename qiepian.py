#L = []
#n = 1
#while n <= 99:
#	L.append(n)
#	n = n + 2

#print(L[-10:])

#L = ['Mike','Search','Tink','Bob','Jack']
#print(L[0],L[1])

#r=[]
#n=3
#for i in range(n):
#	r.append(L[i])
#print(r)

#L=list(range(100))
#print(L[1:2])

#print('ablblbkl'[-4:])

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
	if s.len == 0:
		return u'错误'
	elif s