#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import preprocessing
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression, Lasso
import datetime
from statistics import mean


# In[2]:





# In[ ]:





# In[4]:


data= pd.read_csv("births.csv")


# In[5]:


data


# In[6]:


data.shape


# # MISSING VALUES

# In[7]:


data.isnull()


# In[8]:


data.head(20)


# In[9]:


data.info()


# In[10]:


data.describe()


# In[11]:


data.isnull().sum()


# In[12]:


data.isnull().sum().sum()


# # remove outliers

# In[13]:


sns.displot(data['year'])


# In[14]:


sns.boxplot(data['year'])


# In[15]:


data['year'].mean()


# In[22]:


df=data[data['year']<800]


# In[18]:


df['year'].mean()


# In[19]:


df.shape


# In[20]:


df.boxplot()


# In[21]:


df.hist()


# In[ ]:




