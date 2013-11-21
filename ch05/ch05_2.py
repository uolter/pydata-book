# coding: utf-8
## Data Frame
import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = pd.DataFrame(data)
print frame

frame = pd.DataFrame(data, columns = ['years', 'state', 'pop'])

print frame

frame2 = pd.DataFrame(data, columns = ['years', 'state', 'pop', 'debt'], index = ['one', 'two', 'three', 'four', 'five'])
print frame2

frame2 = pd.DataFrame(data, columns = ['year', 'state', 'pop', 'debt'], index = ['one', 'two', 'three', 'four', 'five'])

print frame2

print frame2.columns
print frame2.index
print frame2['state']
print frame2.state
print frame2.year

print frame2.ix.three
print frame2.ix['three']

import numpy as np

frame2.debt = np.arange(5.)
print frame2
debt = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

frame2.debt = debt

print frame2

# assign a column that does not exist

frame2['eastern'] = frame2.state == 'Ohio'

print frame2
# remouve it 

del frame2['eastern']
print frame2

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print frame3

# Transpose the result
frame3.T
frame3['Ohio'] # column


print frame3['Ohio'][:-1] # skips the last element of the column

print frame3['Nevada'][2:] # it gets elemnts starting at the third position of the column

pdata = { 'Ohio': frame3['Ohio'][:-1],
          'Nevada': frame3['Nevada'][2:]}
print pdate
pd.DataFrame(pdata)

# assigns names at the Indexes
frame3.index.name = 'year'
frame3.columns.name = 'state'

print frame3

print frame3.values # it's an array
