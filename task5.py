#!/usr/bin/env python
# coding: utf-8

# In[3]:


from nltk.corpus import stopwords
stopwords.words('english')


# In[3]:


from nltk.corpus import stopwords
stopwords.words('French')


# In[7]:


from nltk.corpus import stopwords
stopwords.words('german')


# #### 1.2 CMU wordlist

# In[8]:


import nltk 
entries = nltk.corpus.cmudict.entries()
len(entries)


# In[9]:


for entry in entries [10000:10025]:
    print(entry)


# #### 1.3 Wordnet

# In[1]:


from nltk.corpus import wordnet as wn
wn.synsets("phone")
wn.synsets("house")


# In[16]:


wn.synset('call.v.03').lemma_names()


# In[17]:


wn.synset('telephone.n.01').lemma_names()


# In[2]:


wn.synset('family.n.01').lemma_names()


# In[22]:


import nltk
texts = [""" Bare interior.
Grey Light.
 Left and right back, high up, two small windows, curtains drawn. Front right, a door. Hanging near door, its face to wall, a picture. Front left, touching each other, covered with an old sheet, two ashbins. Center, in an armchair on castors, covered with an old sheet, Hamm. Motionless by the door, his eyes fixed on Hamm, Clov. Very red face.
 Brief tableau.
  Clov goes and stands under window left. Stiff, staggering walk. He looks up at window left. He turns and looks at window right. He goes and stands under window right. He looks up at window right. He turns and looks at window left. He goes out, comes back immediately with a small step-ladder, carries it over and sets it down under window left, gets up on it, draws back curtain. He gets down, takes six steps (for example) towards window right, goes back for ladder, carries it over and sets it down under window right, gets up on it, draws back curtain. He gets down, takes three steps towards window left, goes back for ladder, carries it over and sets it down under window left, gets up on it, looks out of window. Brief laugh. He gets down, takes one step towards window right, goes back for ladder, carries it over and sets it down under window right, gets up on it, looks out of window. Brief laugh. He gets down, goes with ladder towards ashbins, halts, turns, carries back ladder and sets it down under window right, goes to ashbins, removes sheet covering them, folds it over his arm. He raises one lid, stoops and looks into bin. Brief laugh. He closes lid. Same with other bin. He goes to Hamm, removes sheet covering him, folds it over his arm. In a dressing-gown, a stiff toque on his head, a large blood-stained handkerchief over his face, a whistle hanging from his neck, a rug over his knees, thick socks on his feet, Hamm seems to be asleep. Clov looks him over. Brief laugh. He goes to door, halts, turns towards auditorium. 
"""]

for text in texts:
    sentences =nltk.sent_tokenize(text)
    for sentence in sentences:
        words =nltk.word_tokenize(sentence)
        tagged_words =nltk.pos_tag(words)
        print(tagged_words)


# ## Task-3 Implementing tokenization

# In[28]:


# Twitter aware Tokenizer
import nltk
from nltk.tokenize import TweetTokenizer
text =' Bare interior.Clov goes and stands under window left. Stiff, staggering walk. He looks up at window left. He turns and looks at window right. He goes and stands under window right. He looks up at window right. He turns and looks at window left. He goes out, comes back immediately with a small step-ladder, carries it over and sets it down under window left, gets up on it, draws back curtain. He gets down, takes six steps (for example) towards window right, goes back for ladder, carries it over and sets it down under window right, gets up on it, draws back curtain. He gets down, takes three steps towards window left, goes back for ladder, carries it over and sets it down under window left, gets up on it, looks out of window. Brief laugh. He gets down, takes one step towards window right, goes back for ladder, carries it over and sets it down under window right, gets up on it, looks out of window. Brief laugh. He gets down, goes with ladder towards ashbins, halts, turns, carries back ladder and sets it down under window right, goes to ashbins, removes sheet covering them, folds it over his arm. He raises one lid, stoops and looks into bin. Brief laugh. He closes lid. Same with other bin. He goes to Hamm, removes sheet covering him, folds it over his arm. In a dressing-gown, a stiff toque on his head, a large blood-stained handkerchief over his face, a whistle hanging from his neck, a rug over his knees, thick socks on his feet, Hamm seems to be asleep. Clov looks him over. Brief laugh. He goes to door, halts, turns towards auditorium.  :) ' 
twtkn =TweetTokenizer()
twtkn.tokenize(text)



# ## Task-4 Frequency Distribution

# In[36]:


# Brown Corpus:
from nltk.corpus import brown
news_text =brown.words(categories ='news')
fdist =nltk.FreqDist(w.lower() for w in news_text)
modals =['can','could','may','might','must','will','what']
for m in modals:
    print(m+ ':',fdist[m],end='\n ')

