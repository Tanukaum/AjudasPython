import subprocess

#Abre aplicação visível ao usuário
notepad = subprocess.Popen(r'C:\Windows\system32\notepad.exe')

#Fecha aplicação
notepad.kill()