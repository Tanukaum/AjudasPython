import pandas as pd

Table1 = {'Column1': ['50', '25', '75', '50', '10'], 'Column2': ['22', '40', '80', '20', '30']}

df= pd.DataFrame(Table1, columns=['Column1', 'Column2'])
Values_to_check = ['10', '30', '20', '25']
number_lines, number_columns = df.shape##Get total lines and colums as int value

for Value_item in Values_to_check: ##Iterate through the list 'UNIQUE'
    for column in df:##Column by column
        for line in range((number_lines)):##Line by line
            if df.loc[line,column] == Value_item:
                df.loc[line,column] = 0 #NewValue
   

print(df)