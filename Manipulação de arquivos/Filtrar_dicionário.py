null = ''

dicionario = [{"statuscode":200,"count":2,"id":"11","pagador":"Outros","categoria":"Aluguel","valor":"680,00","comprovante":null,"name":"Betim","datereg":"2023-02-21 13:31:49"},{"statuscode":200,"count":2,"id":"12","pagador":"Outros","categoria":"Internet","valor":"100,00","comprovante":null,"name":"Betim","datereg":"2023-02-21 13:32:00"}]

def para_txt(texto_para_arquivo):
    with open('file.txt', 'a+') as f:
        f.write('\n' + texto_para_arquivo)

def filtra_dicionario():
    for index in range(len(dicionario)):
        string_para_file = 'Id: ' + dicionario[index]['id'] + '  Pagador: ' + dicionario[index]['pagador'] + '  Categoria: ' + dicionario[index]['categoria'] + '  Valor: ' + dicionario[index]['valor'] + '  Name:  ' + dicionario[index]['name']
        para_txt(string_para_file)

filtra_dicionario()