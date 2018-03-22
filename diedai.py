#d = {'a':1,'b':2,'c':3}
#for key,v in d.items():
#	print(key,v)
#print(d['a'])

#for i,value in enumerate(['a','b','c']):
#	print(i,value)

#for x in [(1,2),(3,4),(5,6)]:
#	print(x)

#a = [0,1,3,2,5,10]
#print(list(range(len(a))))

def find(a):
	t=0
	for i in range(len(a)):
		for x in range(i):
			if a[x] > a[x+1]:
				t=a[x+1]
				a[x+1]=a[x]
				a[x] = t
	return (a[-1:],a[:1]),a
				
#def finddx(L=[]):
#	if len(L)==0:
#		return None,None
#	max = L[0]
#	min = L[-1]
#	for x in L:
#		if x > max:
#			max = x
#		if x < min:
#			min = x
#	return (max,min)
