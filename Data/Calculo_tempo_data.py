from datetime import datetime, timedelta
import time


def print_now_global():
	global now_global
	now_global = datetime.now()
	print(now_global)
	time.sleep(10)


def compara_now_global():
	global now_global
	timeDelta10s = timedelta(seconds=10)#calculos com tempo/datas
	now_real = datetime.now()
	timeMenor = now_real - timeDelta10s

	if now_global < timeMenor:
		print("now_global é menor")
		print(now_global)
		now_global = now_real
		print("novo now_global")
		print(now_global)

print_now_global()

compara_now_global()
