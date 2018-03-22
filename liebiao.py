#L = []
#for x in range(1,11)
#	L.append(x*x)
#print(L)

#d = {'x':'a','y':'b','c':'z'}
#for k,v in d.items(): 
#	print(k,'=',v)

L = ['Hello', 'World', 'IBM', 'Apple',110]

L2=[s.lower() if isinstance(s,str) else s for s in L]
print(L2)