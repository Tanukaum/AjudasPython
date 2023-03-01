import pandas as pd

id = date = time = ['a','b', 'c']

df1 = pd.DataFrame({'Id': id, 'Date': date, 'Hour': time})

df1.to_csv('File.csv', index=False)