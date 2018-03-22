# 内建模块itertools提供了非常有用的用于操作迭代对象的函数
import itertools

# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，
# 根本停不下来
'''
natuals = itertools.count(1)
for n in natuals:
	print(n)
'''
# cycle()会把传入的一个序列无限重复下去	
'''
cs = itertools.cycle('abc')
for c in cs:
	print(c)
'''

# repeat()负责把一个元素无限重复下去，
# 不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A',3)
for n in ns:
	print(n)

# 通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列	
natuals = itertools.count(1)
nn = itertools.takewhile(lambda x:x<=10,natuals)
print(list(nn))
	
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC','XYZ'):
	print(c)
	# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
'''
for key,group in itertools.groupby('AAABBBCCAAA'):
	print(key,list(group))
'''	
# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
#upper()返回小写字母转为大写字母的字符串。
for key , group in itertools.groupby('AaaBBbcCAAa',lambda c:c.upper()):
	print(key,list(group))
	
# 小结
# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，
# 而是Iterator，只有用for循环迭代的时候才真正计算


#练习：
# 计算圆周率可以根据公式：
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：

import itertools
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    nature = itertools.count(1,2) #count(1,2)从1开始，每次+2

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x: x <= (2*N-1), nature)

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    incre = 1
    result = 0
    for n in ns:
        if incre % 2 == 1:
            result = result + (4*1.0/n)
        else:
            result = result - (4*1.0/n)
        incre += 1
    # step 4: 求和:
    return result
	
	
	
	
