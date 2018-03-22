#def fact(n):
#	if n == 1:
#		return n
#	else:
#		return n * fact(n-1)

#尾递归
def fact(n):
	return factiter(n,1)
	
def factiter(num,product):
	if num ==1:
		return product
	else:
		return factiter(num-1,num*product)