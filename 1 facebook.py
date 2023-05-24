#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df =pd.read_csv(r"C:\Users\gaura\OneDrive\Desktop\dataset_Facebook.csv",sep=";")


# In[3]:


df


# In[4]:


df.describe


# In[5]:


df.shape


# In[6]:


sub1=df[['Page total likes','Category','Post Month', 'Post Weekday']].loc[0:15]


# In[7]:


sub1


# In[8]:


sub2=df[['Page total likes', 'Category', 'Post Month', 'Post Weekday']].loc[16:30]


# In[9]:


sub2


# In[10]:


sub3=df[['Page total likes','Category','Post Month','Post Weekday']].loc[30:45]


# In[11]:


sub3


# In[12]:


merge=pd.concat([sub1,sub2,sub3])
merge


# In[13]:


sort=df.sort_values('Page total likes')
sort


# In[14]:


df.transpose()


# In[15]:


shaping=df.shape
shaping


# In[16]:


#reshaping
reshaping=pd.pivot_table(df,index=['Type','Category'],values='like')
print(reshaping)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




