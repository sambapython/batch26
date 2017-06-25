from time import sleep
import threading
from threading import Thread
def fun():
	for i in range(10):
		sleep(1)
		print "fun--->",i 
def fun1():
	for i in range(10):
		sleep(1)
		print "fun1----->",i
t1=Thread(target=fun)
t2=Thread(target=fun1)
t3=Thread(target=fun)
print threading.active_count()
t1.start()
t2.start()
# while True:
# 	if t2.is_alive():
# 		continue
# 	else:
# 		break
t2.join()
t3.start()
print threading.active_count()
print "Main thread executed"