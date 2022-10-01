import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
#Usage of Plotting to create the graphs
df.plot()
plt.show()

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# plt.show()

#df["Duration"].plot(kind = 'hist')

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()