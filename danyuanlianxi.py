#练习：对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	
	def get_grade(self):
		if 80 > self.score >= 60:
			return 'B'
		if 100 >= self.score >= 80:
			return 'A'
		if 60 >= self.score >= 0:
			return 'C'
		else:
			raise ValueError('ValueError')
	

#单元测试类
import unittest

class TestStudent(unittest.TestCase):
	#一个测试方法开始时打印
	def setUp(self):
		print('begin..')
	#一个测试方法结束时打印	
	def tearDown(self):
		print('end...')
	
	def test_80to100(self):
		s1 = Student('Bart',80)
		s2 = Student('Lisa',100)
		self.assertEqual(s1.get_grade(),'A')
		self.assertEqual(s2.get_grade(),'A')
		
	def test_60to80(self):
		s1 = Student('Bart',60)
		s2 = Student('Lisa',79)
		self.assertEqual(s1.get_grade(),'B')
		self.assertEqual(s2.get_grade(),'B')
		
	def test_0to60(self):
		s1 = Student('Bart',0)
		s2 = Student('Lisa',59)
		self.assertEqual(s1.get_grade(),'C')
		self.assertEqual(s2.get_grade(),'C')
		
	def test_invalid(self):
		s1 = Student('Bart',-1)
		s2 = Student('Lisa',101)
		with self.assertRaises(ValueError):
			s1.get_grade()
		with self.assertRaises(ValueError):
			s2.get_grade()
			
if __name__=='__main__':
	unittest.main()
	
	