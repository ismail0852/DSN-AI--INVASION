#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
csv_df=pd.read_csv('New_data.csv')
csv_df


# In[2]:


#For summary of descriptive statistics of the dataframe "variable.describe()"
csv_df.describe()


# In[3]:


csv_df['POPULATION'].mean()


# In[4]:


csv_df['POPULATION'].mode()


# In[5]:


csv_df['POPULATION'].median()


# In[6]:


csv_df['POPULATION'].count()


# In[7]:


#To show even more information about the dataset
csv_df.info()


# In[8]:


#To show the features in the datasets
csv_df.columns


# In[9]:


#Indexing in pandas: process of retrieving datas in a dataset
#Square bracket notation to access all observations of selected features
# print out states column as pandas series
print(csv_df['STATES'])

#Print out state column as Dataframe
print(csv_df[['STATES']])

#print out Dataframe with states and puplation columns
print(csv_df[['STATES', 'POPULATION']])


# In[10]:


print(csv_df[0:10])


# In[11]:


print(csv_df[4:6])


# In[12]:


#Using Loc and Iloc
#Since the dataset contains no label-based index, we can only use interger based iloc
#Print out observation for the third 
print(csv_df.iloc[9])
#pint out observation for the 4th and 5th state
print(csv_df.iloc[6:10])


# In[13]:


print(csv_df.iloc[10:20])


# In[14]:


print(csv_df[10:20])


# In[15]:


print(csv_df.iloc[32])


# In[16]:


#Drop rows of column called population
df=csv_df.drop(['POPULATION'],axis=1)
print(df)


# In[ ]:





# In[22]:


#changing the datatype of features for series object
df['POPULATION']=df['POPULATION'].astype('float')
df

#or with the use of downcasting
pd.to_numeric(df['POPULATION'],downcast='integer')


# In[ ]:





# In[23]:


#adding ga new column using the existing columns in Dataframe
df['AreaPopu']= df['AREA']+df['POPULATION']
df.columns


# df=csv_df.drop(['POPULATION'],axis=1)
# print(df)

# In[35]:


df=csv_df.append(['POPULATION'])
print(df)


# In[36]:


df.sort_index(inplace=True,ascending=False)
df


# In[ ]:




