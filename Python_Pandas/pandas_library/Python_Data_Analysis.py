import pandas as pd

#read the csv and store it inside the dataframes
df = pd.read_csv('data.csv')
#print the number of columns
print(df.columns)

#to have the data information
df_info = df.info
print(df_info)

#to have all the describe information about the data
print(df.describe())

#to get about specific column
print(df.describe()['Calories'])

print('*********************************************************************************')

grouped_df = df.groupby(['Calories']).max()
print(grouped_df['Pulse'])

print('*********************************************************************************')
#it will give the occurence of the values for which value is equal to 108
print(df[df['Pulse'] == 108])
df1 = df[df['Pulse'] == 108]

#print the value of the particular cell
print(df1['Calories'][140])