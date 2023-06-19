#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[50]:


file_path = 'D:\\Project\\FIFA_data_cleaning\\fifa21_raw_data.csv'


# In[51]:


data = pd.read_csv(file_path)
data


# In[52]:


data.info()


# In[53]:


data.columns


# In[54]:


numerical_features = data.select_dtypes(include = 'number').columns.tolist()
categorical_features = data.select_dtypes(exclude = 'number').columns.tolist()


# In[55]:


numerical_features


# In[56]:


categorical_features


# In[33]:


data.isnull().sum().head(60)


# In[57]:


data.shape[0]


# In[58]:


data1 = data.dropna()
data1


# In[59]:


data1.shape[0]


# In[60]:


data.loc[:,'Growth':'Wage']


# In[61]:


data['Loan Date End'].unique()


# In[62]:


data['Loan Date End'].fillna(value = 'not_closed', inplace = True)
data['Loan Date End'].unique()


# In[63]:


encoding = data['Name'].dtype
encoding


# In[64]:


pip install chardet


# In[65]:


import chardet


# In[66]:


with open('D:\\Project\\FIFA_data_cleaning\\fifa21_raw_data.csv', 'rb') as rawdata:
    result = chardet.detect(rawdata.read(1000000))
print(result)


# In[67]:


data['Name'].head(20)


# In[68]:


data['Height'].head()


# In[69]:


data2= data['Height']
data2


# In[70]:


data2 = data2.astype(float)


# In[71]:


data['Height'] = data['Height'].astype(float)


# In[72]:


# Function to remove newline characters from a string
def remove_newlines(s):
    if isinstance(s, str):
        return s.replace('\n', '')

# Apply the function to all columns using applymap()
data = data.applymap(remove_newlines)
data


# In[73]:


data['Name'].head(20)


# In[74]:


data['Joined']


# In[75]:


data['Joined'] = pd.to_datetime(data['Joined'])
data['Joined'].dtype


# In[76]:


import datetime
current_date = datetime.date.today()
current_date


# In[77]:


current_date = pd.to_datetime(datetime.date.today())
data['Joined'] = pd.to_datetime(data['Joined'])
data['years_played'] = (current_date - data['Joined']).dt.days/365
data['years_played']


# In[78]:


data['Value']


# In[79]:


data['Value'] = pd.to_datetime(data['Value'])


# In[80]:


data = data.drop(['photoUrl','LongName','playerUrl'], axis = 1)


# In[81]:


data.info()


# In[82]:


col = list(data.columns)
data.columns = [x.strip().lower() for x in col]


# In[83]:


data['team & contract']


# In[84]:


def split_team_contract(cols):
  cols = cols.str.replace(r'^[\n]{4}', '')
  cols = cols.str.replace(r'[\n]{2}', '')
  cols_split = cols.str.split('\n', 1, expand=True)
  if len(cols_split.columns) == 2:
    data['team'] = cols_split[0]
    data['contract'] = cols_split[1]
  else:
    data['team'] = cols_split[0]
    data['contract'] = None  # Set to None or any other appropriate value
  return cols

data['team & contract'] = split_team_contract(cols=data['team & contract'])
data = data.drop(columns=['team & contract'])


# In[85]:


data.info()


# In[86]:


data['height']


# In[87]:


def convert_height(height):
    feet, inches = height.split("'")
    feet = int(feet)
    inches = int(inches.strip('"'))
    total_inches = feet*12 + inches
    cm = total_inches * 2.54
    return cm

data['height_cm'] = data['height'].apply(convert_height)


# In[88]:


data['height_cm']


# In[89]:


data.describe(include = 'object')


# In[91]:


data['joined']


# In[93]:


data['height']


# In[99]:


data['height'].drop


# In[101]:


data['height_cm']


# In[104]:


data = data.drop(['height'], axis = 1)


# In[105]:


data.info()


# In[107]:


data.weight.value_counts()


# In[108]:


data.club.value_counts()
