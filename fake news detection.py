#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import preprocessing
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression, Lasso
import datetime
from statistics import mean


# In[19]:


data= pd.read_csv("train.csv")


# In[20]:


data


# In[21]:


data.shape


# # MISSING VALUES

# In[22]:


data.isnull()


# In[23]:


data.head(20)


# In[24]:


data.info()


# In[25]:


data.describe()


# In[26]:


data.isnull().sum()


# In[27]:


data.isnull().sum().sum()


# # remove outliers

# In[28]:


sns.displot(data['Label'])


# In[30]:


sns.boxplot(data['Label'])


# In[31]:


data['Label'].mean()


# In[32]:


df=data[data['Label']<40]


# In[33]:


df['Label'].mean()


# In[34]:


df.shape


# In[35]:


df.boxplot()


# In[36]:


df.hist()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




