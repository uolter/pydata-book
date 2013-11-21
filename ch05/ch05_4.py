# coding: utf-8
from pandas import Series, DataFrame
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print s1, s2
s1 + s3
s1 + s2
s1
s2
s1 + s2
s1 + s2 # NA values in the indeces that don't overlap.
list('bcd')
import numpy as np
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1 + df2 # unions of rows and columns
df1
df2
# Arithmetic value with fill value
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df1 + df2
df1.add(df2, fill_value=0)
df1
df2
df1.add(df2, fill_value=0)
# operations between daframe and series
arr = np.arange(12.).reshape((3, 4))
arr
arr[0] # first row
arr[0] # first row, which is again an array
arr - arr[0]
arr - arr[1]
arr - arr[0]  # this is referred as broadcasting
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
series = frame.ix[0]
frame
series
frame - series # broadcasting down the rows
series2 = Series(range(3), index=['b', 'e', 'f'])
series2
frame
frame + series2
series3 = frame['d']
frame.sub(series3, axis=0)
series3
