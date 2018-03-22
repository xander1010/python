class Student(object):
	name = 'student'
	def __init__(self,name):
		self.name = name

#实例化对象		
s = Student('bob')

#实例属性优先级高于类属性
print(s.name)

#但类属性不会消失
print(Student.name)

#删除实例的name属性，显示的就是类的name属性了
del s.name
print(s.name)

#练习：为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Stu(object):
	count = 0
	
	def __init__(self,name):
		self.name = name
		Stu.count += 1

#实例化对象，查看类的统计数量
the1 = Stu('lisa')
print(Stu.count)

the2 = Stu('lily')
print(Stu.count)