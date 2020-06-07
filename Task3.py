#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk


# In[6]:


nltk.download()


# In[11]:


from nltk.corpus import inaugural


# In[12]:



inaugural.fileids()


# In[13]:


from nltk.corpus import brown


# In[14]:



brown.categories()


# In[15]:



inaugural.words(fileids='2009-Obama.txt')[:20]


# In[16]:



from nltk.book import *


# In[18]:


f=FreqDist(text7)


# In[19]:


f


# In[21]:


print (f)


# In[22]:


f.most_common(50)

