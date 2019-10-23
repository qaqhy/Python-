#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from sklearn.decomposition import PCA
t = pd.read_csv('../../机器学习/day1/test.csv')
t1 = pd.read_csv('../../机器学习/day1/test1.csv')
t2 = pd.read_csv('../../机器学习/day1/test2.csv')
m = pd.merge(t, t1, on=['A', 'A'])
m = pd.merge(m, t2, on=['A', 'A'])
print(m)
print(m.head(10))


# In[6]:





# In[ ]:




