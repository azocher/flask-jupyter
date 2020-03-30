#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

def export(data):
    baby_names = pd.read_csv(data)
    return baby_names['Gender'].value_counts()


# In[ ]:




