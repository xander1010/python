class Test(object):
	__slots__ =("name",)
	
	def __init__(self,name):
		self.name = 3
	def da(self):
		print('1')
		
d = Test(1)

d.da()

d.name = 2

print(d.name)

# d.age =1

