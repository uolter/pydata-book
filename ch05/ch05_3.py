# coding: utf-8

## Index Objects
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index

print index
print index[1:]
print index[1]
index[1] = 'd' # index objects are immutable and thus can't be modified by the user.

# index object can be shared safely among data structure

import numpy as np
index = pd.Index(np.arange(3))
obj2 = pd.Series([1.5, -2.5, 0], index=index)
print obj2
obj2.index is index


pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print frame3

'Ohio' in frame3.columns
2003 in frame3.index

## Reindexing
from pandas import Series

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print obj
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print obj2
obj = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print obj
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

# interpolation or filling
obj3.reindex(range(6), method='ffill')
print obj3
obj3.reindex(range(6), method='pad')
obj3.reindex(range(6), method='bfill')

# with dataframe

from pandas import DataFrame
frame = DataFrame(np.arange(9).reshape(3,3), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print frame
frame2 = frame.reindex(['a','b', 'c', 'd'])
print frame2
states = ['Texas', 'Utah', 'California']
frame.reindex(columns = states)
frame.reindex(index= ['a', 'b', 'c', 'd'], columns = states ,)
frame.reindex(index= ['a', 'b', 'c', 'd'], columns = states,
method='ffill')

# Dropping entries from an axis 

obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print obj
new_obj = obj.drop('c')
print new_obj
obj.drop(['d', 'c'])
data = DataFrame(np.arange(16).reshape((4,4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print data
data.drop(['Colorado', 'Ohio'])
data.drop('two', axis=1) # it drops the second column
data.drop(['two','four'], axis=1) # it drops the second and founth column
# Indexing, selection and filtering
obj = = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj == Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print obj
obj['b']

obj[1]
obj[1] == obj['b']
obj[2:4]
obj[['b', 'a', 'd']]
obj[[1,3]]
print obj
obj < 2
obj[obj < 2]
obj['b':'c']

# setting using this method
obj['b':'c'] = 5
print obj
data
data['two'] # second column
data[['three', 'one']] # it the third and first column
data[:2]
data[:2] # it gets only the first 2 rows
data
data['three'] > 5
data[ data['three'] > 5]
data < 5
data[data < 5]
data[data < 5] = 0
print data
data.ix['Colorado', , ['two', 'three']] # second row, second and third column
data.ix['Colorado',  ['two', 'three']] # second row, second and third column
data.ix[['Colorado', 'Utah'],  [3, 0, 1]] 
print data
data.ix[2] # third row
print data
data.ix[:'Utah', 'two']
data.ix[:'Utah', 'two'] # till Utah, second column
data.three > 5
data.ix[data.three > 5, :3]
