computador = ['a','b','c']
ids = ['0','1','2']
cores = ['azul', 'verde', 'rosa']
dicionario = dict()
dicionario2 = dict()
for pc in range(len(computador)):
    dicionario[computador[pc]] = {'ip': ids[pc], 'cor':cores[pc]}
    dicionario2[pc] = ids[pc], cores[pc]



print(dicionario['a']['ip'])
print(dicionario2[0][0])

print(dicionario)
print(dicionario2)