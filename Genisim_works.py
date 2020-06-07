#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from gensim.models import Word2Vec
import numpy as np


# In[23]:


df = pd.read_csv('data.csv')
df.head(3)


# In[10]:


df['Maker_Model']= df['Make']+ " " + df['Model']


# In[14]:


df1 = df[['Engine Fuel Type','Transmission Type','Driven_Wheels','Market Category','Vehicle Size', 'Vehicle Style', 'Maker_Model']]
df2 = df1.apply(lambda x: ','.join(x.astype(str)), axis=1) 
df_clean = pd.DataFrame({'clean': df2}) 
sent = [row.split(',') for row in df_clean['clean']]
sent[:2]


# In[15]:



model = Word2Vec(sent, min_count=1,size= 50,workers=3, window =3, sg = 1)


# In[16]:


model['Toyota Camry']


# In[17]:


model.similarity('Porsche 718 Cayman', 'Nissan Van')


# In[18]:


model.similarity('Porsche 718 Cayman', 'Mercedes-Benz SLK-Class')


# In[21]:


## Show the most similar vehicles for Mercedes-Benz SLK-Class : Default by eculidean distance 
model.most_similar('Mercedes-Benz SLK-Class')[:5]

