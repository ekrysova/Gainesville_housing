#!/usr/bin/env python
# coding: utf-8

# Gainesville, Housing data

# In[30]:


#Importing data
import pandas as pd
import numpy as np

df=pd.read_excel('GainesvilleHomes.xlsx')
df


# In[31]:


df.info()


# In[32]:


#Working with missing Data
samp=df.loc[1:15]
samp.head(15)


# In[33]:


#Identifying missing data
samp.isna()


# In[34]:


#Removing missing data
samp.dropna()


# In[35]:


#Change column names
df.columns


# In[36]:


df.columns = (['East West ', 'North South', 'Beds+Bath', 'Square Feet', 'Lot Size',
       'Commute to UF', 'Year Built', 'Days', 'ES', 'MS', 'HS','Price',
       'Price(thousands)'])


# In[37]:


df


# In[38]:


#Removing a column
df.drop('Days', axis=1)


# In[39]:


#Shrinking the data frame: Shrink the Data frame down to just the "Lot Size" and "East-West" columns, getting rid of the missing data and then displaying the average lot size for an "East" Home compared to a "West" Home
df.drop(columns=['North South', 'Beds+Bath', 'Square Feet','Commute to UF', 'Year Built', 'Days', 'ES', 'MS', 'HS','Price','Price(thousands)'],inplace=True)


# In[40]:


df


# In[54]:


df.dropna()


# Properties of Dataframe: The data contains information about the houses on the market in Gainesville, Florida.This is an excel file which was imported to Python. It orginally had 28 rows and  13 columns which were manipulated throughout the exercise. I started off by renaming and  identifying the missing inputs throughtout the data frame. I changed some of the column names and then removed a column that I felt was not needed in the dataframe. Afterwards, I went ahead and shrunk the data frame down to two columns 'East West' and 'Lot Size'.
