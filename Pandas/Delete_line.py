import pandas as pd
import os

path_file = (os.path.realpath(os.curdir) + '\\Files\\Book.xlsx')

df = pd.read_excel(path_file)

print(df)

df = (df.drop(axis=0,labels=1))

print(df)