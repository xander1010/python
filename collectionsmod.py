# p = (1,2)
# 看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场

from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
# 调用时按定义的对应x或y来取值，方便识别
print(p.x,p.y)

# 用坐标和半径表示一个圆，也可以用namedtuple定义：
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle',['x','y','r'])


print('################deque#############')

from collections import deque

# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
# 这样就可以非常高效地往头部添加或删除元素
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

print('################defaultdict#############')
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict

dd = defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
#不存在时
print(dd['key2'])

print('################OrderedDict#############')
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict

d = dict([('a',1),('b',2),('c',3)])
# dict的key是无序的
print(d)

od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)

odd = OrderedDict()
odd['z'] = 1
odd['y'] = 2
odd['x'] = 3
# 按照插入key的顺序返回
print(list(odd.keys()))

# OrderedDict可以实现一个FIFO（先进先出）的dict，
# 当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

	def __init__(self,capacity):
		super(LastUpdatedOrderedDict,self).__init__()
		self._capacity = capacity
		
	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:',last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value)
		
print('################Counter#############')

# Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter

c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
	
# 取出现最多的前3项
d = Counter('abscsdsd').most_common(3)
print(d)
	
print(c)

# Counter实际上也是dict的一个子类，上面的结果可以看出，
# 字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次

	
	





