import json, os

file_1 = os.path.dirname(os.path.realpath(__file__)) + '\\Files\\json_1.json' 
file_2 = os.path.dirname(os.path.realpath(__file__)) + '\\Files\\json_2.json'

#Abre arqueivo 1, modo leitura
with open(file_1,'r') as f:
    data_1 = json.load(f)

#Abre arqueivo 2, modo leitura
with open(file_2,'r') as f2:
    data_2 = json.load(f2)

    #Busca e altera o campo no arquivo 2
    for item in range(len(data_1['Times'])):
        if data_2['Times'][item]['Nome']['opcional'] == data_1['Times'][item]['Nome']['opcional']:
            data_2['Times'][item]['Nome']['base'] = (data_1['Times'][item]['Nome']['base'])

#Abre arquivo 2, modo escrita e salva as mudanças
with open(file_2, 'w') as f2:
    json.dump(data_2, f2)

print('Fim')
