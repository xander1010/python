# 任何对象，只要正确实现了上下文管理，就可以用于with语句。

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
'''
class Query(object):

	def __init__(self,name):
		self.name = name 
		
	def __enter__(self):
		print('Begin')
		return self
		
	def __exit__(self,exc_type,exc_value,traceback):
		if exc_type:
			print('Error')
		else:
			print('End')
	
	def query(self):
		print('Query info about %s...'%self.name)
		
	def hello(self):
		print('hello')

#with语句时先执行__enter__,再执行调用的方法，最后执行__exit__		
with Query('Bob') as q:
	q.query()
	q.hello()
'''

# @contextmanager
# 编写__enter__和__exit__仍然很繁琐
# 标准库contextlib提供了更简单的写法，上面的代码可以改写如下
from contextlib import contextmanager

class Query(object):
	
	def __init__(self,name):
		self.name = name
		
	def query(self):
		print('Query info about %s...' %self.name)
		
@contextmanager
def create_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')

with create_query('Bob') as q:
	q.query()

# @contextmanager这个decorator接受一个generator(生成式）
# 希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
	print("<%s>" %name)
	yield
	print("<%s>" %name)
	
with tag("h1"):
	print('hello')
	print("world")

# 代码的执行顺序是：

# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>。
# 因此，@contextmanager让我们通过编写generator来简化上下文管理


# 如果一个对象没有实现上下文，我们就不能把它用于with语句。
# 这个时候，可以用closing()来把该对象变为上下文对象。
# 例如，用with语句使用urlopen()
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
	for line in page:
		print(line)
		
# closing也是一个经过@contextmanager装饰的generator，
# 这个generator编写起来其实非常简单：
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
# 它的作用就是把任意对象变为上下文对象，并支持with语句。

# @contextlib还有一些其他decorator，便于我们编写更简洁的代码。





