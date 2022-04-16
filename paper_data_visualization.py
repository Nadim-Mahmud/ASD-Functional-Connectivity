import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

PATH = r"D:\Project\Data\Practice\time_series_after_flatening\AngularGyrus.csv"

df = pd.read_csv(PATH).values

d1 = df[0]
d2 = df[19]

t1 = df[1]
t2 = df[20]

t1 = t1[1:101]
t2 = t2[1:101]

d1 = d1[1:101]
d2 = d2[1:101]

d1 = np.append(d1, t1)
d2 = np.append(d2, t2)

x = [range(1, 201)]

print(len(x), d1.shape)

plt.scatter(x, d1, color = 'red', marker='o', label='Control')
plt.scatter(x,d2, color = 'green', marker='v', label='Patient')

plt.legend()
plt.show()
plt.savefig('data_scatter.jpg')


