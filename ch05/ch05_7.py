# coding: utf-8
from pandas import Series
## Hierarchical Indexing 
data = Series(np.random.randn(10),
index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
import numpy as np
data = Series(np.random.randn(10),
index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
data
data.index
data[b]
data['b']
data['b': 'c']
data.ix[['b', 'd']]
# selection in an inner level
data[:, 2]
data.unstack()
data.unstack().stack()
from pandas import DataFrame
frame = DataFrame(np.arange(12).reshape((4, 3)),
index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
columns=[['Ohio', 'Ohio', 'Colorado'],
['Green', 'Red', 'Green']])
frame
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame
# Reordering and Sorting Levels
frame.swaplevel('key1', 'key2')
frame.sortlevel(1)
# Summary Ststistics by Level
frame.sum(level='key2')
