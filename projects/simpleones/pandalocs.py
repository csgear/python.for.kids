import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(16).reshape((4,4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], 
    columns=['one', 'two', 'three', 'four'])

# print(data)

# print(data.iloc[1])

# print(data.loc['Ohio'])

# print(data.loc[:, data.one > 1])

s1 = data.loc['Ohio', 'one']

s2 = data.iloc[0, 0]

print(s1)

print(s2)
