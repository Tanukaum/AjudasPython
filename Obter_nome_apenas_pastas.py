import os

current_dir = os.scandir()

for file in current_dir:
	if file.is_dir():
		print(file.name)