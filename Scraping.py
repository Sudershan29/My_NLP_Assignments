#!/usr/bin/env python
# coding: utf-8

# ###  Scraping Web Using Beautiful Soup

# In[1]:


import bs4


# In[2]:


import requests


# In[3]:


page=requests.get("https://www.quora.com/");


# In[4]:


print(page.status_code)
#print("The 200 status code is by far the most common returned. It means, simply, that the request was received and understood and is being processed.")


# In[5]:


l=bs4.BeautifulSoup(page.content,'html.parser');


# In[6]:


print(l.title.string)


# ####  Using Prettify Object we can print the HTML Content of the Page

# In[7]:


print(l.prettify())


# In[8]:


list(l.children)


# In[ ]:




