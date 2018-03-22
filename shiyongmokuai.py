# -*- coding:utf-8 -*-

#任何模块代码的第一个字符串都被视为模块的文档注释
'a test module'

#添加作者信息，个人理解方便查找是谁写的
__author__ = 'Xander'

#正文
import sys

def test():
	args = sys.argv
	if len(args)==1:
		print('Hello,world!')
	elif len(args)==2:
		print('Hello,%s!'%args[1])
	else:
		print('too many arguments!')
		
if __name__ == '__main__': #此处可判断是调用还是直接执行以作输出
	test()
	
# __author__ 表示特殊变量 

# _abc / __abc 表示私有的,private，不应该被引用

# abc / test 表示公共的，public

#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

def _private1(name):
	return 'hello,%s!'%name
def __private2(name):
	return 'hi,%s!'%name
	
def greeting(name):
	if len(name) > 3:
		return _private1(name)
	else:
		return __private2(name)

print(greeting("kl"))
	