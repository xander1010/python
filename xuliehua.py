# 序列化，把一个变量从内存变为可存储或传输过程
# 用pickle模块来实现序列化
import pickle

d = dict(name='Bob',age = 20,score =88)
#序列化成一个bytes
pickle.dumps(d)

#把序列化后的bytes写入一个文件对象
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

#反序列化
f = open('./test/dump.txt','rb')

# 直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
d = pickle.load(f)
f.close()
print(d)

#也可以用pickle.loads()方法反序列化出对象

# 将python对象变成一个json
import json

#dump()方法可以直接把JSON写入一个file-like Object
#dumps()方法返回一个str，内容就是标准的JSON
d = dict(name='Bob',age = 20,score =88)
json.dumps(d)

#将json反序列化，
# 用loads()或者对应的load()方法，前者把JSON的字符串反序列化，
# 后者从file-like Object中读取字符串并反序列化
json_str = '{"name": "Bob", "age": 20, "score": 88}'
json.loads(json_str)


# 将一个实例对象序列化为json对象
def stu2dict(std):
	return {
			'name':std.name,
			'age':std.age,
			'score':std.score
	}

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
	
s = Student('Bob',20,99)

# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象
print(json.dumps(s,default=stu2dict))

# 把任意class的实例变为dict：通常class的实例都有一个__dict__属性
#有少数例外，比如定义了__slots__的class
print(json.dumps(s, default=lambda obj: obj.__dict__))




#将json反序列化为一个Student对象实例
def dict2stu(d):
	return Student(d['name'],d['age'],d['score'])
	
	
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# 传入的object_hook函数负责把dict转换为Student实例
print(json.loads(json_str,object_hook=dict2stu))

a = json.loads(json_str,object_hook=dict2stu)
print(a.name)



#练习：中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响
import json

boj = dict(name = '小明',age = 20)
s = json.dumps(boj,ensure_ascii = True)

print(s)









