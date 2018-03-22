#sum=0
#ages = [1,2,3,4,5,6]
#for age in range(101):
#	sum=sum+age
#print(sum)
#a=list(range(11))
#print(a)


#sum = 0
#n = 99
#while n > 0:
#	sum = sum + n
#	n = n-2
#print (sum)

names = ['boy','lili','lucy','mary']
for n in names:
	if n == 'lucy':
		break
	print('hello,',n)
print('++++++++++++++++++++++++++++++++++++++++++++++')	
s = 1
while s <= 100:
	if s > 5:
		break
	print(s)
	s = s + 1
print('END')
print('++++++++++++++++++++++++++++++++++++++++++++++')	
m=0
while m <10:
	m=m+1
	if m % 2 == 0:#如果m是偶数，执行continue
		continue #直接进行下一轮循环，这次就不print
	print(m)
print('++++++++++++++++++++++++++++++++++++++++++++++')	

while 1>0:
	print (u"是呀是呀")#这个是死循环



