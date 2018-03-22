class Student(object):
	# __slots__ = ('name','score')
	
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
		
	#将方法转换成属性，获取的方法
	@property
	def get_name(self):
		return self.__name
	@property
	def get_score(self):
		return self.__score
	
	#将设置方法转换成属性，
	@get_score.setter
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError(u'请输入整数')
		if value < 0 or value > 100:
			raise ValueError(u'请输入0 - 100 的整数')
		self.__score = value


#实例化对象	
s = Student('xander',95)

#因为是私有变量，这里的变量属性不是原来的
s.name = "lala"
s.score = 89
#可以得到结果，不是实例对象时的属性
print(u'新加的属性：',s.name,s.score)
print('the shili name:',s.get_name,s.get_score)

#实际就是调用实际转化为s.set_score(30)
s.set_score = 30

print(s.get_score)

#理解练习
class Test(object):
	@property  #要使用这个，变量就为私有，_或__开头
	def birth(self):
		return self._birth
	@birth.setter	#可读写
	def set_birth(self,value):
		self._birth = value
	@property  #可读
	def age(self):
		return 2017 - self._birth

a = Test()
#转换成属性了，所以直接赋值
a.set_birth = 1988
print('the birthday year is:',a.birth)
print('the age is :',a.age)	
	
print('##########下面是练习题###########')
#练习：利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter	
	def set_width(self,width):
		self._width = width
	@property	
	def height(self):
		return self._height
	@height.setter
	def set_height(self,height):
		self._height = height
	@property	
	def resolution(self):
		return self._width * self._height
		
# 测试:
b = Screen()
b.set_width = 1024
b.set_height = 768
print('resolution =', b.resolution)
if b.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')





	
	
	
	
	

