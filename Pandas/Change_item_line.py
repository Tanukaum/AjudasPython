import pandas as pd
df= pd.DataFrame({'Column1': ['C1L0', 'C1L1', 'C1L2'], 'Column2': ['C2L0', 'C2L1', 'C2L2'], 'Column3':[' ','C3L2 ',' ']})
number_lines, number_columns = df.shape##Get total lines and colums as int value

condition = ' '

for column in range(number_columns-1):##Column by column except the Column3
    for line in range((number_lines)):##Line by line 
        previous_line = line - 1
        if df.loc[line,'Column3'] != ' ':
            df.loc[previous_line,'Column2'] = df.loc[line,'Column3']

print(df)