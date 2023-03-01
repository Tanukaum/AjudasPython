import pandas as pd

id = date = time = ['a','b', 'c']

df = pd.DataFrame({'Id': id, 'Date': date, 'Hour': time})


#Se for ser passado para um excel:
df.to_excel('Sheet.xlsx', 'Sheet1', index=False, header=False)

df_semIndices= df.to_string(index=False, header=False)

print('COM:  ')
print(df)

print('SEM:  ')
print(df_semIndices)