import math

def quadratic(a,b,c):

	if b**2-4*a*c < 0:
		print("该方程无解")
	else:
		x1 = (-b + math.sqrt(b**2-4*a*c)) / (2 * a)
		x2 = (-b - math.sqrt(b**2-4*a*c)) / (2 * a)
		return x1, x2
a = 2
b = 3
c = 1
print(quadratic(a, b, c))