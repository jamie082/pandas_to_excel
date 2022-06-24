import pandas as pd
import openpyxl

# forming dataframe
df = pd.DataFrame ([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
    index=['Jamie', 'Lindsey', 'Susan'], columns=['a', 'b', 'c'])

# storing into the excel file
df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')

print(df)