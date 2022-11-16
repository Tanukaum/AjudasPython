import os

path = 'C:\\Users\\juliof\\OneDrive - The Walt Disney Company\\Fernando M Julio\\Temp\\iHOPs\\'
folder_list = ['Engine01', 'Engine02', 'Engine03', 'Engine04', 'Engine07', 'Engine08', 'Engine09', 'Octo03', 'Octo04', 'Octo05', 'Octo06']
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
        