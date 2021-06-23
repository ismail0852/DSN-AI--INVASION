#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
data=[['Ayo',10,'NY'],['Imran',15,'OS'],['Chucks',14,'MA']]
df=pd.DataFrame(data,columns=["Name","Age",'State'])
df


# In[6]:


data={'Name':['Ayo','Imran','Chucks'],'Age':[10,15,14],'State':['NY','0S','MA']}
df=pd.DataFrame(data)
df


# In[11]:


dict_data={'State':['Abia','Adamawa','Lagos','Osun','Rivers'],'Capital':['Umuahia','Yola','Ikeja','Osogbo','Portharcourt'],'Area':[6320,36917,3345,9251,11077],'Population':[2845380,3178950,9113605,3416959,5198605]}
df=pd.DataFrame(dict_data)
df


# In[13]:


student_inform={'FirstName':['ismail','khalid','ibrahim','Clinton'],'LastName':['Sulaiman','olayiwola','odedoye','Harry'],'Department':['Networking and System Security','Software ENgineering','Hardware Engineering','NIL'],'MatricNo':['NSS_2019_009','CSE_2019_010','CHE_2019_011','NIL']}
df=pd.DataFrame(student_inform)
df


# In[24]:


#import csv file using pd.read_csv
csv_df=pd.read_csv('Data_2006.csv')
csv_df


# In[29]:


#import csv file using pd.read_csv
excel_df=pd.read_excel('Desktop/Excel.xlsx')
excel_df


# In[ ]:





# In[ ]:





# In[ ]:




