import os

current_dir = os.scandir()

for file in current_dir:
	if file.is_dir() and file.name.startswith('W'):
		print(file.name, file.path)