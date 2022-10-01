import pandas as pd

#by default the first sheet will get printed
df = pd.read_excel('Python_Pandas_Practice.xlsx')
print(df)

#we can aslo pass the specific Sheet name whch we want to print
df = pd.read_excel('Python_Pandas_Practice.xlsx', sheet_name= 'Address_Sheet2' )
print(df)

print(type(df))

#Now get the value of the particular sheet
#Nw get the value of cell
print(df.get('City'))

#to get the particular city value
print(df.get('City')[1])

print('*************************************************************************************************')
#load all the sheets - and use dataframe as a key to get particular sheet name
df_sheet_all = pd.read_excel('Python_Pandas_Practice.xlsx', sheet_name=None)
#to get the first sheet
print(df_sheet_all['Address_Sheet'])
#To get the country from first sheet
print(df_sheet_all['Address_Sheet']['Country'])
#to get the 2nd country value
print(df_sheet_all['Address_Sheet']['Country'][1])
print(df_sheet_all['Address_Sheet2'])
#to get the state from second sheet value
print(df_sheet_all['Address_Sheet2']['State'])
#to get the second State values
print(df_sheet_all['Address_Sheet2']['State'][1])