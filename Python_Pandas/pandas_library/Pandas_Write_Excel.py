import pandas as pd
import openpyxl

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

print(df)
#         a   b   c
# one    11  21  31
# two    12  22  32
# three  31  32  33

#save the dataframe to the excel and specify the sheet name
#df.to_excel('pandas_new_update.xlsx' , sheet_name='Updated_Values')

df2 = df[['a', 'c']]
print(df2)

# with pd.ExcelWriter('pandas_new_update.xlsx') as writer:
#     df.to_excel(writer, sheet_name='sheet1')
#     df2.to_excel(writer, sheet_name='sheet2')


#Append to an exisitng file
# path = 'pandas_new_update.xlsx'
# #if we give the sheet name - it will append the data to the existing file
# with pd.ExcelWriter(path) as writer:
#     writer.book = openpyxl.load_workbook(path)
#     df.to_excel(writer, sheet_name='new_sheet1')
#     df2.to_excel(writer, sheet_name='new_sheet2')
