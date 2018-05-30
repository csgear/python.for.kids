
import pandas as pd 
import numpy as np

obj = pd.Series([7,-5,7,4,2,0,4])

# print(obj.rank())

# print(obj.rank(method='min', ascending=False))

# print(obj.rank(method='max', ascending=True))

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], 
    index=['a', 'b', 'c', 'd'], columns=['one', 'two'])

print(df.sum())

print(df.sum(axis=1))

print(df.idxmax())