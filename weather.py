#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import preprocessing
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression, Lasso
import datetime
from statistics import mean


# In[20]:


data= pd.read_csv("weather.csv")


# In[21]:


data


# In[22]:


data.shape


# In[23]:


#MISSING VALUES


# In[24]:


data.isnull()


# In[25]:


data.info()


# In[26]:


data.describe()


# In[27]:


data.isnull().sum()


# In[28]:


data.isnull().sum().sum()


# In[29]:


data.head()


# In[ ]:





# In[ ]:





# # remove outliers

# In[40]:


sns.displot(data['RISK_MM'])


# In[42]:


sns.boxplot(data['RISK_MM'])


# In[43]:


data['RISK_MM'].mean()


# In[48]:


df=data[data['RISK_MM']<40]


# In[51]:


df['RISK_MM'].mean()


# In[53]:


df.shape


# In[54]:


df.boxplot()


# In[55]:


df.hist()


# In[ ]:




