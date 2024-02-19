import pandas as pd
import os

path = (os.path.realpath(os.curdir) + '\\Files\\')

df= pd.DataFrame({'Column1': ['C1L0', 'C1L1', 'C1L2'], 'Column2': ['C2L0', 'C2L1', 'C2L2'], 'Column3':['C3L1','C3L2 ','C3L3']})
number_lines, number_columns = df.shape##Get total lines and colums as int value

df.to_excel(path + 'Book.xlsx')