import pandas as pd

Table1 = {'Column1': ['50', '25', '75', '50', '10'], 'Column2': ['22', '40', '80', '20', '30']}

df= pd.DataFrame(Table1, columns=['Column1', 'Column2'])
Values_to_check = ['10', '20', '25', '30']

for value in Values_to_check:
    df.loc[df['Column1'] == value, 'Column1'] = 'Não válido'
    df.loc[df['Column2'] == value, 'Column2'] = 'Não válido'

print(df)