import os

path = 'path to folder'
folder_list = ['name', 'name', 'name']
text_to_search = 'Test'

for folder in folder_list:
    files_list = os.listdir(path + folder)
    for file in files_list:
        file_opened = open(path + folder + '\\' + file, 'r')
        try:
            lines = file_opened.readlines()
        except Exception as e:
            print('Exception: ' + str(file) + ' - ' + str(e))
        
        for linha in lines:
            if text_to_search in linha:
                print('Text Found!')
        