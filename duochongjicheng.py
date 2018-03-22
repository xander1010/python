class Animal(object):
	def a(self):
		print('This is Animal.')
	
class FlyableMixln(object):
	def f(self):
		print('This is Flyable.')
	
class Runnable(object):
	def r(self):
		print('This is Runnable.')

#多重继承和Mixln ,在创建的类名后加个Mixln,便于区分，不加也可以		
class New(Animal,FlyableMixln,Runnable):
	def n(self):
		print('This is New_Class')

#实例化		
test = New()

test.a()
test.n()
test.f()
test.r()

