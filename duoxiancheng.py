import time,threading

#新线程执行的代码
def loop():
	print('thread %s is running..'%threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>%s'%(threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.'%threading.current_thread().name)
	
print('thread %s is running..'%threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.'%threading.current_thread().name)

		
#Lock

#假定以下是你的银行存款：
balance = 0	
#创建Lock实例	
lock = threading.Lock()

def change_it(n):
	#先存后取，结果应该为0：
	global balance
	balance = balance + n
	balance = balance - n
	
def run_thread(n):
	for i in range(1000000):
		#先获取锁
		lock.acquire()
		try:
			#放心改了
			change_it(n)
		finally:
			#改完后要释放锁
			lock.release()
	
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



		