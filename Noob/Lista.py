lista_vazia = []
lista_preenchida = ['a','b', 'c']

def check_lista(lista):
    if len(lista) == 0:
        print('\nLista vazia')
        print(lista)
    else:
        print('\nLista não vazia! Elementos: ')
        print(lista)

check_lista(lista_vazia)

check_lista(lista_preenchida)