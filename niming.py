#关键词lambda代表匿名函数
print(list(map(lambda x:x*x,[1,2,3,4,5,6])))

# 把匿名函数作为值返回
def build(x,y):
	return lambda x,y:x*x+y*y

f = build(3,4)
#lambda后面加上x,y，那输入的就没有意义了，返回时是按后面输入的来计算。
print(f(4,4))

# 练习：

L = list(filter(lambda n : n%2==1,range(1,20)))
print(L)