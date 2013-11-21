# coding: utf-8
import pandas as pd
obj = pd.Series([4, 7, -5, 3])
obj
obj.values
obj.index
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
obj.index
obj2.index
obj2['a']
obj2['d']
obj2[['c', 'a', 'd']]
## Array operations
obj2
obj2[obj2 > 0]
np
import numpy as np
obj2 * 2
np.exp(obj2)
'b' in obj2
'e' in obj2
# create a series from a python data dictionary
sdata = {'Ohio': 35000, 'Texas': 71000', 'Oregon': 16000, 'Utah': 5000}
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
obj3
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
obj4
pd.isnull(obj4)
pd.notnull(obj4)
obj4.isnull()
obj3; obj4
obj3
obj4
obj3 + obj4
obj4.name = 'population'
obj4.index.name = 'state'
obj4.values
obj4
obj
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj
