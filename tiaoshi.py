def foo(s):
	n = int(s)
	# print('>>>n = %d'%n)
	#用print来辅助查看的地方，都可以用断言来替代
	# 启动Python解释器时可以用-O(O是大写的O)参数来关闭assert
	assert n != 0,'n is zero'
	return 10 / n
	
def main():
	return foo('1')
	
print(main())

print('+++++++++++next+++++++++++++++')
#用logging模块调试，。。
import logging
logging.basicConfig(level=logging.INFO)

s ='1'
n = int(s)
logging.info('n = %d'%n)
print(10/n)

print('+++++++++++next+++++++++++++')
#python的调试器，pdb
#以参数-m pdb启动，小写l查看代码，n运行下一行代码，单步调试
#只有执行变量完了后 p + 变量名，可以查看变量，q可以结束调试
s = '1'
n = int(s)
print(10/n)


print('+++++++++++next+++++++++++++')
#pdb.set_trace() ,在可能出错的地方放一个，就能设置一个断点
# 要先导入pdb
import pdb 
s = '0'
n = int(s)
#加一个断点，运行到这儿,自动跳到pdb调试，可以用P查看变量，或c继续运行
pdb.set_trace()
print(10/n)

#要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE






