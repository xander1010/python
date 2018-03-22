# std1 = {'name':'michael','score':98}
# std2 = {'name':'bob','score':88}

# def print_score(std):
	# print('%s:%s'%(std['name'],std['score']))

# print(print_score(std1))

class Student(object):

	def __init__(self,name,score):
		self.name = name
		self.score = score
			
	def print_score(self):
		print('%s:%s'%(self.name,self.score))
		
bart = Student('Bart Simposon',59)
lisa = Student('Lisa Simpson',87)

bart.print_score()
lisa.print_score()