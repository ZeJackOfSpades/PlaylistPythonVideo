#coding:utf-8
import time
import threading

myLock	=	threading.RLock()

class MyProcess(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		i = 0
		while i < 3:
			with myLock:			#Verrouillage de la tache (section critique)
				letters	=	"ABC"
				for lt in letters:
					print(lt)
					time.sleep(0.3)
			i += 1

"""
def processOne():
	i = 0
	while i < 3:
		print("oooooooo")
		time.sleep(0.3)
		i += 1

def processTwo():
	i = 0
	while i < 3:
		print("xxxxxxxx")
		time.sleep(0.3)
		i += 1
"""
"""
th1	=	threading.Thread(target=processOne)
th2	=	threading.Thread(target=processTwo)
"""
th1	=	MyProcess()
th2	=	MyProcess()

th1.start()
th2.start()

th1.join()
th2.join()

print("Fin du programme")