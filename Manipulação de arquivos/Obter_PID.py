import psutil

string = r'C:\Program Files\Vizrt\Viz3\viz.exe -u1 -y -n'
for process in psutil.process_iter():
	try:
		if process.name() == 'viz.exe' :
			print(process.name())
			print(process.cmdline())
			print(process.pid)
	except psutil.AccessDenied: 
		pass

