import pandas as pd
from scipy.stats import trim_mean
import numpy as np
import wquantiles
state =pd.read_csv('data\state.csv')
#평균
state.head()
state['Population'].mean()
#절사평균 극단에서 10%를 제거함
trim_mean(state['Population'],0.1)
#중간값
state['Population'].median()
#인구에 가중치를 준 살인율에 대한 가중평균
np.average(state['Murder.Rate'],weights=state['Population'])
#인구에 가중치를 준 살인율에 대한 가중중간값
wquantiles.median(state['Murder.Rate'],weights=state['Population'])


ax = (state['Population']/1_000_000).plot.box()
ax.set_ylabel('Population (millions)')

import matplotlib.pyplot as plt
plt.figure(dpi=100)
plt.ylabel('Population (millions)')

ax = (state['Population']/1_000_000).plot.hist(density = True, xlim =[0,12],bins = range(1,12) ,figsize=(4,4))
state['Murder.Rate'].plot.density(ax=ax)
plt.show()

import pandas as pd

lc_loans = pd.read_csv('https-github.com-gedeck-practical-statistics-for-data-scientists\data\lc_loans.csv')
lc
crosstab = lc_loans.pivot_table(index ='grade')