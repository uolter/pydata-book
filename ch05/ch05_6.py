# coding: utf-8
from pandas import DataFrame
from pandas import DataFrame, Series
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj.index.is_unique
obj['a']
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
import numpy as np
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df.ix['b']
## Summarizing and Computing Descriptive Statistics
# reductions or summary statistics
f = DataFrame([[1.4, np.nan], [7.1, -4.5],
[np.nan, np.nan], [0.75, -1.3]],
index=['a', 'b', 'c', 'd'],
columns=['one', 'two'])
df
df = DataFrame([[1.4, np.nan], [7.1, -4.5],
[np.nan, np.nan], [0.75, -1.3]],
index=['a', 'b', 'c', 'd'],
columns=['one', 'two'])
df
df.sum() # columns sum
df.sum(axis=1) # sum row by row
df
(7.10 - 4.5)/2
df.mean(axis=1, skipna=False)
df
df.idxmax()
df
df.cumsum() # accumultation
df.describe() # multiple summary statistics in one shot.
obj = Series(['a', 'a', 'b', 'c'] * 4)
obj
obj.describe()
## Correlation and Covariance
import pandas.io.data as web
all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
    
price = DataFrame({tic: data['Adj Close'],
for tic, data in all_data.iteritems()})
price = DataFrame({tic: data['Adj Close'] 
for tic, data in all_data.iteritems()})
price
volume = DataFrame({tic: data['Volume'] 
for tic, data in all_data.iteritems()})
# percent changes of the prices:
returns = price.pct_change()
returns.tails()
returns.tail()
returns.MSFT.corr(returns.IBM) # correlation of the overlapping non-NA
returns.MSFT.cov(returns.IBM) # covariance of the overlapping non-NA
returns.corr()
returns.cov()
returns.corrwith(returns.IBM)
returns.corrwith(volume)
## Unique values, Value counts, and membership
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
uniques
obj.value_counts()
obj.value_counts() # value frequencies
from pandas import value_counts
value_counts(obj.values, sort=False)
obj
mask = obj.isin(['b', 'c'])
obj[mask]
mask
data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
'Qu2': [2, 3, 1, 2, 3],
'Qu3': [1, 5, 2, 4, 4]})
data
data.Qu1
data.Qu1.value_counts
data.Qu1.value_counts()
result = data.apply(value_counts).fillna(0)
resutl
result
## Handling Missing Data
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data
string_data.isnull
string_data.isnull()
string_data[0] = None
string_data.isnull()
string_data
# Filtering out Missing Data
from numpy import nan as NA
data = Series([1, NA, 3.5, NA, 7])
data.dropna()
data[data.notnull()]
data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
[NA, NA, NA], [NA, 6.5, 3.]])
data
cleaned = data.dropna()
cleaned
cleaned = data.dropna() # it drops every row which contains at least one Na value
data.dropna(how='all') # it only drops row with all value equals to NA
data[4] = NA
data
data.dropna(axis=1, how='all')
## Filling in Missing Data
df
df.fillna(0)
df = DataFrame(np.random.randn(7, 3))
df
df.ix[:4,1]
df.ix[:4,1] = NA
df.ix[:4,1]
df.ix[:2, 2] = NA
df
df.dropna(thresh=3)
df
df.fillna({1: 0.5, 3:-1})
df
_ = df.fillna(0, inplace=True)
df
a = 5
_ = a +3
a
df = DataFrame(np.random.randn(6, 3))
df.ix[2: ,1] = NA
df.ix[4: ,2] = NA
df
df.fillna(method='ffill')
df
df.fillna(method='ffill', limit=2)
data = Series([1., NA, 3.5, NA, 7])
(1. + 3.5 + 7) /3
