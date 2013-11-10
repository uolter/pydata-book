import pandas as pd

tot_lang = [('c', 18),
 ('javascript', 2),
 ('java', 15),
 ('scala', 1),
 ('python', 13),
 ('f', 2),
 ('ruby', 2)]

tot = [t[1] for t in tot_lang]


index = [i[0] for i in tot_lang]

a =pd.Series(tot, index= index)
a.sort()
pd.Series.plot(a, kind='bar')

import matplotlib.pyplot as plt
plt.show()
