def power(x,y=3):
	if y<0:
		return "y can't small than 0"
	else:
		s = 1
		while y > 0:
			y = y - 1
			s = s * x
	return s

print(power(3,7))

#参数化，求一个数的多少次方