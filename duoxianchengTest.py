#在多核CPU下，这个死循环不会跑满CPU
import threading,multiprocessing

def loop():
	x = 0
	while True:
		x = x ^ 1
	
for i in range(multiprocessing.cpu_count()):#获取CPU核心数
	# 创建线程
	t = threading.Thread(target = loop)
	t.start()
	
# 启动与CPU核心数量相同的N个线程
# 但执行代码时，其实多线程在Python中是交替执行，所以基本也只用了一个CPU
# 可以利用多进程实现多核任务
