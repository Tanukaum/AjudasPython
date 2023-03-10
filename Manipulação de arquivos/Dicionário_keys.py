computador = ['a','b','c']
ips = ['0','1','2']
cores = ['azul', 'verde', 'rosa']
dicionario = dict()
dicionario2 = dict()
for pc in range(len(computador)):
    dicionario[computador[pc]] = {'ip': ips[pc], 'cor':cores[pc]}
    dicionario2[pc] = ips[pc], cores[pc]



print(dicionario['a']['ip'])
print(dicionario2[0][0])

print(dicionario)
print(dicionario2)