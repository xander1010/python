import os

'''
print('Process (%s) start...'%os.getpid())
#只能在unix/linux/mac上运行
pid = os.fork()
if pid == 0:
	print('I am child process (%s) and my parent is %s'%(os.getpid(),os.getppid()))
else:
	print('I (%s) just created a child process (%s)'%(os.getpid(),pid))
	

运行结果如下：

Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.	
'''
'''	
from multiprocessing import Process

#子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)..'%(name,os.getpid()))
	
if __name__=='__main__':
	print('Parent process %s.'%os.getpid())
	# 创建子进程时，只需要传入一个执行函数和函数的参数，
	# 创建一个Process实例
	p = Process(target=run_proc,args=('test',))
	print('Child process will start.')
	# 进程启动
	p.start()
	#等待子进程结束后再继续运行，用于进程间同步
	p.join()
	print('Child process end.')
	
'''
# print('++++++++以下是Pool的内容++++++++++')

'''
#启动大量子进程，用进程池的方式批量创建子进程	
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print('Run task %s (%s)..'%(name,os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.'%(name,(end - start)))
	
if __name__=='__main__':
	print('Parent process %s.'%os.getpid())
	#Pool同时处理与CPU核心数有关
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('Waiting for all subprocesses done..')
	#要调用close()后才能调用join
	p.close()
	p.join()
	print('All subprocesses done.')
'''
	
#子进程
import subprocess

#nslookup是域名查询
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)	

#子进程需要输入，通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:',p.returncode)	
	

	
#process间通信有Queue,Pipes等来交换数据
from multiprocessing import Process,Queue
import os,time,random

#写数据进程执行的代码
def write(q):
	print('Process to write:%s'%os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue..'%value)
		q.put(value)
		time.sleep(random.random())
		
#读数据进程执行的代码
def read(q):
	print('Process to read:'%os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue..'%value)
		
#父进程创建Queue,并传给各个子进程
q = Queue()
pw = Process(target=write,args=(q,))
pr = Process(target=read,args=(q,))
#启动子进程pw，写入：
pw.start()
#启动子进程 pr,读取：
pr.start
#等待pw结束
pw.join()
#pr进程里是死循环，无法等待结束，只能强行终止：
pr.terminate()






	
	