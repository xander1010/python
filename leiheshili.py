class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	
	def print_score(self):
		print('%s:%s'%(self.name,self.score))
		
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
	
		
#实例化	
bart = Student('Mike',80)

#分别打印出bart,Student
# print(bart,Student)

#可以自由的给实例绑定属性，甚至修改已有的属性
bart.age = 8
print(bart.age)

#直接在实例对象上调用print_score()方法
print(bart.print_score())

#调用Student类的get_grade()方法
print('成绩为：',bart.get_grade())


#再定义函数，相当于把方法拿出来了，没有封装在类里面
def print_sc(std):
	print('%s:%s'%(std.name,std.score))

print(print_sc(bart))

# 我的理解：这里类的属性就是参数，方法是函数



