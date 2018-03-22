class Student(object):
	pass
	#限制实例的属性 ,后面是一个元组tuple
	# __slots__ = ('name','age')

	
s = Student()
	
def set_age(self,age):
	self.age = age 
	

from types import MethodType
#给实例绑定一个方法，通过MethodType，只对当前实例有效
s.set_age = MethodType(set_age,s)

s.set_age(25)
print(s.age)

def set_score(self,score):
	self.score = score

#给类绑定一个方法，所有实例都可以用
Student.set_score = set_score

s.set_score(85)
print(s.score)

s2 = Student()
s2.set_score(99)

print(s2.score)
