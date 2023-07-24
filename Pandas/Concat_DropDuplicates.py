import pandas as pd

id = date = time= local = ['a','a_1']

id_2 = date_2 = time_2 = local_2 = ['a','b','c']

df = pd.DataFrame({'Id': id, 'Date': date, 'Hour': time, 'PGM/PVW': local})

df_2 = pd.DataFrame({'Id': id_2, 'Date': date_2, 'Hour': time_2, 'PGM/PVW': local_2})   

df = pd.concat([df, df_2])
new_df = df.drop_duplicates(keep='first')
print(new_df)