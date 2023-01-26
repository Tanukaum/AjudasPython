import os

path_files = 'C:\\Temp'

list_files = (os.listdir(path_files))
for file in list_files:
	if file.endswith('.pdf'):
		print(file)