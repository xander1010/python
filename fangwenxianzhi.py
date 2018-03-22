class Student(object):
	def __init__(self,name,score,gender):
		#实例的变量以__开头，表示为私有变量，外部不能直接用self.name = 11来更改
		self.__name = name
		self.__score = score
		#练习里将gender设置为不可访问
		self.__gender = gender
	
	#因设置为私有变量，所以此方法不能直接访问了
	def print_score(self):
		print('%s : %s'%(self.__name,self.__score))
	
	# 增加方法访问name和score
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	
	#增加修改值的方法,在方法中，可以对参数做检查
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
	
	def get_gender(self):
		return self.__gender
	#练习加的属性	
	def set_gender(self,gender):
		if self.__gender in ('male','female'):
			self.__gender = gender
		else:
			raise ValueError('bad gender')
	

#实例化对象
bart = Student('Bart',87,'male')

#这种修改并没有修改到原来的变量，只是新增了一个变量
bart.__name = "the new"

print(bart.__name)
print(bart.get_name())

# 调用 方法
print(bart.set_score(88))
print(bart.get_score())

#测试练习

if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')