# coding: utf-8
## Functional application and mapping
import numpy as np
from pandas import DataFrame
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
f = lambda x: x.max() - x.min()
frame.apply(f)
frame.apply(f) # this apply f to each column
frame.apply(f, axis=0) # this apply f to each column
frame.apply(f, axis=1) # this apply f to each row
# apply can retuern a series
from pandas import Series
def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)
frame
frame.apply(f, axis=1)
# compute a formatted string
format = lambda x: '%.2f' % x
frema.apply(format)
freme.apply(format)
frame.apply(format)
frame.applymap(format)
map = frame.applymap(format)
map
map.__class__
frame['e']
frame['e'].map(format)
## Sorting and ranking
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
columns=['d', 'a', 'b', 'c'])
frame
frame.sort_index()
frame.sort_index(axis=1)
frame.sort_index(axis=1, ascending=False)
frame.sort_index(axis=1, ascending=True)
frame
obj = Series([4, 7, -3, 2])
obj.order()
obj = Series([4, np.nan, 7, np.nan, -3, 2])
obj.order()
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame
frame.sort_index(by='b')
frame.sort_index(by=['a', 'b']) # sort by multiple columns
obj = Series([7, -5, 7, 4, 2, 0, 4])
obj.rank()
obj.mean()
obj.rank(method='first')
obj.rank(ascending=False, method='max')
frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
'c': [-2, 5, 8, -2.5]})
frame
frame.rank(axis=1)
get_ipython().system(u'ls')
