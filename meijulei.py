from enum import Enum

Month = Enum('month',(('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')))

for name,member in Month.__members__.items():
	print(name, '==>',member,',',member.value) #value属性自动赋给成员的int常量，默认从1开始计数


from enum import unique	

@unique  #这个装饰器可以检查保证没有重复值
class Weekday(Enum):
	Sun = 0 #Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
	
	
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday(1))
# print(weekday(7))

#__members__是一个特殊变量，想成是in 一个字典
for name,member in Weekday.__members__.items():
	print(name,'==>',member)
	
	
#练习：把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum,unique 

@unique
class Gender(Enum):
	Male = 0
	Female = 1
	
class Student(object):

	def __init__(self,name,gender):
		if not isinstance(gender,Gender):
			raise TypeError('gender must be enum value')
		self.name = name
		self.gender = gender
	

s = Student('Wangjia',Gender.Male)
print(s.name,':',s.gender)
	
# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
	
	
	
	
	
