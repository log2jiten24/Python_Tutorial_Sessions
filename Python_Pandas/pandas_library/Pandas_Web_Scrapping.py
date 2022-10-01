import pandas as pd

# Webpage url
url = 'https://en.wikipedia.org/wiki/History_of_Python'

# Extract tables
dfs = pd.read_html(url)
#print(dfs)

# Get first table
df = dfs[0]

# Extract columns
df2 = df[['Version','Release date']]
print(df2)

#Now lets write the content to an excel
df2.to_excel('Python_Data_Scrap.xlsx', sheet_name='Data_Scrap')