class Dict(dict):
	def __init__(self,**kw):
		#super()让这里的__init__也可以用继承对象dict里的__init__参数
		super().__init__(**kw)
	
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attr'%s'"%key)
			
	def __setattr__(self,key,value):
		self[key] = value



d = Dict(a=1, b=2)
print(d['a'])
print(d.a)


#编写单元测试
import unittest

# from danyuanceshi import Dict

class TestDict(unittest.TestCase):

	def setUp(self):
		print('setUp..')
		
	def tearDown(self):
		print('tearDown..')

	
	#每个测试方法以test_xxx开头
	def test_init(self):
		d = Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
		
	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')
		
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
			
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

#可以加上以下语句直接执行单元测试脚本			
if __name__=='__main__':
	unittest.main()
	
#也可以在命令行通过参数-m unittest直接运行单元测试
#可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试	
	

print('+++++以下是练习+++++++++')

#练习见：danyuanlianxi.py	
	
	
	
	
	
	
	
	
	
	