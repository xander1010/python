#操作文件和目录，都在OS模块下
import os

#查看当前操作系统类型，nt为windows，posix为linux,unix或mac os x
os.name 

#获取更详细的信息，windows不支持
# os.uname

#在操作系统中定义的环境变量都在os.environ中
os.environ

# 要获取某个环境变量的值
os.environ.get('PATH')
#取x,如果没有就返回default
os.environ.get('x','default')

#查看当前目录的绝对路径
f = os.path.abspath('.')
print(f)

#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
#用os.path.join()来合并路径
f1 = os.path.join(f,'testdir')
print(f1)

#创建上面已列好的目录
# os.mkdir(f1)
# print('has created')

#删除对应的目录
# os.rmdir(f1)
# print('has deleted')

#用os.path.split()来拆分路径，拆分最后一个
#合并拆分不要求目录或文件真实存在
f2 = os.path.split('E:/python/file/haha.txt')
print(f2)

#获取文件扩展名
f3 = os.path.splitext('E:/python/file/pic.png')
print(f3)


#重命名文件和文件夹
# os.rename('test1','test')
# print('has renamed')

# 删除文件或目录
# os.remove('E:/python/test/te.txt')
# print('has removed')

#列出当前目录下所有目录
L = [x for x in os.listdir('.') if os.path.isdir(x)]
print(L)

#列出当前目录下所有.py文件
L1 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(L1)



#练习：
#1、利用os模块编写一个能实现dir -l输出的程序。
import os

def dir_l():
    print(os.listdir('.'))

#2、编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
import os

def foundfile(s,path = ''):
	for p in [x for x in os.listdir(path)]:
		tmp = os.path.join(os.path.abspath(path),p)
		if os.path.isfile(tmp):
			if os.path.splitext(p)[0].find(s) != -1:
				print(os.path.join(os.path.abspath(path),p))
		if os.path.isdir(tmp):
			foundfile(s,tmp)

#群里的方法
def get_files(file_name):
    for root, dirs, files in os.walk(os.path.abspath(".")):  # 获取当前目录的所有子目录和文件
        for file_path in files:
            if file_name in file_path:
                print(os.path.join(root, file_path))
#调用方法查找并打印路径
foundfile('caozuowenjian','E:/python')














