import requests
from pandas.io.json import json_normalize
import pandas as pd

url = "https://api.exchangerate-api.com/v4/latest/USD"
df = pd.read_json(url)
print(df)

df.to_json('examples.json')

#Now lets read the json file

df_json = pd.read_json('examples.json')

df_json.to_csv('Examples.csv')

# json string
s = '{"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"x","row2":"y","row3":"z"}}'

# read json to data frame
df = pd.read_json(s)
print(df)
df.to_json('examples_02.json')

