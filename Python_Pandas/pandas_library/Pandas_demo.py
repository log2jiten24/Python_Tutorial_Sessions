import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
#to print in the DataSet Format
myvar = pd.DataFrame(mydataset)
print(myvar)

#to get the pandas version
print(pd.__version__)

#A Pandas Series is like a column in a table.

#It is a one-dimensional array holding data of any type.
a = [1, 7, 2]
myvar = pd.Series(a)

print(myvar[0])


a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

print(myvar["x"])

#to load the json file

df = pd.read_json('C:\\Users\\ACER\\OneDrive\\Desktop\\Selenium steps\\Python Tutorials\\Python_Pandas\\TestData\\json_payload.json')
print(df.to_string())


print('**************************************************************************')
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)