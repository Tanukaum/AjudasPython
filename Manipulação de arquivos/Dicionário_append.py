d = dict()

for a in range(2):
    d[a] = (a+1),(a+2)

print("Original:" )
print(d)

#Obtém a última posição com len() e insere valor nela
d.update({len(d):(3,4)})
d.update({len(d):(4,5)})

print(d)