class Animal(object):
	def run(self):
		print('Animal is running...')
	
class Dog(Animal):
	def run(self):
		print('Dog is running...')
	
	def eat(self):
		print('Eating meat...')

	
class Cat(Animal):
	def run(self):
		print('Cat is runnig...')
	

#新加一个Tortoise类
class Tortoise(Animal):
	def ru(self):
		print('Tortoise is running slowly')
	
	
	
dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 定义一个类时相当于定义了一种数据类型
a = list()
b = Animal()
c = Dog()
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Animal))


#理解多态的好处？新加一个字类，不用对函数做修改，父类有run方法
def run_twice(animal):
	animal.run()
	animal.run()
	
run_twice(Tortoise())



