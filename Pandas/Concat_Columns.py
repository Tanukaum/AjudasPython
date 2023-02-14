import pandas as pd

id = date = time = ['a','b', 'c']

df = pd.DataFrame({'Id': id, 'Date': date, 'Hour': time})

df['ConcatColumns'] = df.apply(lambda x: '%s.%s.%s' % (x['Id'],x['Date'],x['Hour']), axis=1)

print(df)