lista = [1,2,3,4,5,6]

# Execução normal
print('Todos Valores: ')
for item in lista:
    if item == 4:
        print(item)
    elif item%2 == 0:
        print(item, 'par')
    else:
        print(item,'impar')

# Execução com break
print('Usando BREAK')
for item in lista:
    if item == 4:
        break
    elif item%2 == 0:
        print(item, 'par')
    else:
        print(item,'impar')

# Execução com continue
print('Usando continue')
for item in lista:
    if item == 4:
        continue
    elif item%2 == 0:
        print(item, 'par')
    else:
        print(item,'impar')