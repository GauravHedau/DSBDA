#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import bs4


# In[2]:


var1=requests.get('https://www.flipkart.com/boat-airdopes-161-asap-charge-10mm-drivers-17-hours-playback-bluetooth-headset/p/itm8a7493150ae4a?pid=ACCG6DS7WDJHGWSH&lid=LSTACCG6DS7WDJHGWSH4INU8G&marketplace=FLIPKART&q=boat+bluetooth&store=0pm%2Ffcn%2F821%2Fa7x%2F2si&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&fm=search-autosuggest&iid=en_sHywjeQDlUsLC6y6inq3SymvGtD8tXI4wMha%2B8gm4l1NoxM9aWVxIHDWPsBbNIWrdHtWcWSBepfdoA2tlbrNFg%3D%3D&ppt=sp&ppn=sp&ssid=65d981cn8w0000001684815489645&qH=988e01db83eaac2e')
var1


# In[3]:


var1.content


# In[14]:


var2= bs4.BeautifulSoup(var1.text)


# In[20]:


overall=var2.find('div',{'class':'_2d4LTz'}).get_text()
overall


# In[18]:


inividual=var2.findAll('div',{'class':'_3LWZlK _1BLPMq'})
for i in inividual:
    print(i.get_text()+'\n')


# In[19]:


r=var2.find_all('div',{'class':'t-ZTKy'})
for j in r:
    print(j.get_text()+'\n')


# In[12]:


cutname=var2.find_all('span',{'class':'_2GEIK5'})
for k in cutname:
    print(k.get_text()+ '\n')


# In[ ]:




