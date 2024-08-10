#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


# In[2]:


data= pd.read_csv("C:\\Users\\praya\\Downloads\\archive (11)\hotel_bookings.csv")
data.head()


# In[3]:


data.dtypes


# In[4]:


data.info()


# In[5]:


data.describe()


# In[6]:


data['children'].unique


# In[41]:


# no duplicates
data.duplicated()


# In[43]:


# check for missing values:
data.isnull().sum()


# In[42]:


# check for missing values:
data.isnull().sum()


# In[47]:


#plotting box plot b
sns.boxplot(x='arrival_date_month', y='stays_in_weekend_nights', data=data)


# In[46]:


data['stays_in_weekend_nights'].describe()

