import pandas as pd
id = ['0','1','2']
date = ['10-10','10-11','10-12']
local = ['a','b','c']

df = pd.DataFrame({'Id': id, 'Date': date, 'local': local})

comp = ['big', 'small', 'big']

df_2 = pd.DataFrame({'Id': id, 'Complement': comp})

df['Complement'] = df_2['Complement']

print(df)
df.c