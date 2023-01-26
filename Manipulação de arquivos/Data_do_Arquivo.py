import time
import os

file_path = 'C:\Temp\IMG_TEST.png'

file_time_C = time.ctime(os.path.getctime(file_path)) #Data de Criação
file_time_M = time.ctime(os.path.getmtime(file_path)) #Data de Modificação

file_date_C = time.strptime(file_time_C)
file_date_M = time.strptime(file_time_M)

print(file_date_C)
print(file_date_M)