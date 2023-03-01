import pandas as pd

Table1 = {'Tamanho': ['P', 'P', 'M', 'G', 'G'], 'Tipo': ['Camisa', 'Calça', 'Jaqueta', 'Meia', 'Camisa'], 'Cor': ['Azul', 'Verde', 'Azul', 'Preto', 'Rosa']}

df= pd.DataFrame(Table1, columns=['Tamanho', 'Tipo', 'Cor'])

df_filter1 = df[df.Tipo.isin(['Camisa','Calça'])]

print(df_filter1)

df_filter2 = df[df.Cor.isin(['Azul'])][df[df.Cor.isin(['Azul'])].Tipo.isin(['Camisa'])]
#df_filter2 = df_filter2[df_filter2.Tipo.isin(['Camisa'])]     
print(df_filter2)