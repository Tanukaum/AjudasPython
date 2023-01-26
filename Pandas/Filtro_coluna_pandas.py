import pandas as pd

Table1 = {'Tamanho': ['P', 'P', 'M', 'G', 'G'], 'Tipo': ['Camisa', 'Calça', 'Jaqueta', 'Meia', 'Camisa'], 'Cor': ['Azul', 'Verde', 'Azul', 'Preto', 'Rosa']}

df= pd.DataFrame(Table1, columns=['Tamanho', 'Tipo', 'Cor'])

df_filter = df[df.Tipo.isin(['Camisa','Calça'])]

print(df_filter)