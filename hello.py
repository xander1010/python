#name = input('please enter your name:')
#print('hello,',name)
#print('1024*768=',1024*768)

#a = -1
#if a >=0:
#	print(a)
#else:
#	print(-a)

#s1=72
#s2=85
#r=s2-s1
#print('成绩提升了%d%%'%r)

h=float(input('your height:'))
w=float(input('your weight:'))
h2=h*h
bmi=w/h2
if bmi <18.5:
	print('过轻')
elif 18.5<=bmi<25:
	print('正常')
elif 25<=bmi<28:
	print('过重')
elif 28<=bmi<32:
	print('肥胖')
else:
	print('肥胖严重')	
	
	