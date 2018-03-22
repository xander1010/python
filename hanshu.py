def myabs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('The Type is worry')
	if x >= 0:
		return x
	else:
		return -x

