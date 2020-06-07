#!/usr/bin/env python
# coding: utf-8

# # Cosine similarity

# In[88]:


X="""The Greek Wikipedia (also Hellenic Wikipedia, Elliniki Vikipedia, Greek: Ελληνική Βικιπαίδεια) is the Greek-language edition of Wikipedia, the free online encyclopedia. It was started on December 1, 2002. It surpassed the 10,000 article mark on May 16, 2006 and the 100,000 article mark on April 9, 2014. As of May 23, 2019, it is the 46th largest Wikipedia, behind Belarusian and ahead of Slovene.


The community of Greek Wikipedia has organized some meetups as well. Since 2011, the Wikimedia User Group Greece has aided in the organization of various promotional activities, as well and some article contests.

Η Ελληνική Βικιπαίδεια (επίσης Ελληνική Βικιπαίδεια, Ελληνική Βικιπαίδεια, Ελληνική: Ελληνική Βικιπαίδεια) είναι η ελληνική έκδοση της Wikipedia, η δωρεάν διαδικτυακή εγκυκλοπαίδεια. Ξεκίνησε την 1η Δεκεμβρίου 2002. Ξεπέρασε το 10.000 σήμα άρθρου στις 16 Μαΐου 2006 και το 100,000 άρθρο στις 9 Απριλίου 2014. Από τις 23 Μαΐου 2019, είναι η 46η μεγαλύτερη Wikipedia, πίσω από τη Λευκορωσία και μπροστά από Σλοβενικά

Greek Wikipedia is the main free internet encyclopedia written in Greek. Its main competitor, Livepedia, started on 2004, had more than 100.000 articles. Many articles of Livepedia were republished articles from donations of various publishing houses and the site was also a wiki. Approximately 250 articles are coming at least partially from Livepedia, thanks to the Livepedia's use of GFDL until November 1, 2008. As of 2018, Greek Wikipedia's pageviews surpassed the 250 million annually.Η Ελληνική Βικιπαίδεια είναι η κύρια δωρεάν εγκυκλοπαίδεια Διαδικτύου γραμμένη στα Ελληνικά. Ο κύριος ανταγωνιστής της, η Livepedia, ξεκίνησε το 2004, είχε περισσότερα από 100.000 άρθρα.The daily pageviews of Greek Wikipedia vary within the year; peaking in the winter period (late November to mid March), while the months with the least pageviews are usually June, July and August.[1] The active users are more than 1,000 today (as of May 15, 2019). The highest and lowest active users' numbers are recorded in the same period.

Πολλά άρθρα της Livepedia αναδημοσιεύθηκαν άρθρα από δωρεές διαφόρων εκδοτικών οίκων και ο ιστότοπος ήταν επίσης ένα wiki. Περίπου 250 άρθρα προέρχονται τουλάχιστον εν μέρει από τη Livepedia, χάρη στη χρήση του GFDL από τη Livepedia έως την 1η Νοεμβρίου 2008. Από το 2018, οι προβολές σελίδας της ελληνικής Wikipedia ξεπέρασαν τα 250 εκατομμύρια ετησίως. Οι καθημερινές προβολές σελίδας της ελληνικής Wikipedia ποικίλλουν εντός του έτους. κορυφώνεται στη χειμερινή περίοδο (τέλη Νοεμβρίου έως μέσα Μαρτίου), ενώ οι μήνες με τις λιγότερες προβολές σελίδας είναι συνήθως Ιούνιος, Ιούλιος και Αύγουστος. [1] Οι ενεργοί χρήστες είναι περισσότεροι από 1.000 σήμερα (από τις 15 Μαΐου 2019). Οι υψηλότεροι και χαμηλότεροι αριθμοί ενεργών χρηστών καταγράφονται την ίδια περίοδο.

Η κοινότητα της ελληνικής Wikipedia έχει οργανώσει επίσης συναντήσεις. Από το 2011, η Ομάδα χρηστών του Wikimedia Greece έχει βοηθήσει στη διοργάνωση διαφόρων διαφημιστικών δραστηριοτήτων, καθώς και σε ορισμένους διαγωνισμούς άρθρων."""

print(X)


# In[ ]:





# In[93]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import string

f=open("compare.txt",'r')
Y=f.read()
f.close();
  
# tokenization 
X_list = X.split(' ')
Y_list = Y.split(' ')


# sw contains the list of stopwords 
sw = stopwords.words('english') 
sw = sw + stopwords.words('greek') 
l1 =[];l2 =[] 
  
# remove stop words from string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
  
# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine) 
f.close()


# # TESTING

# In[81]:


m=stopwords.words('greek') 
a=bytes("διαφόρων",encoding="utf-8")
print(a)


# In[82]:


b='Η Ελληνική halo halo'
s=b.split(' ')
def is_hex(s):
    for j in s:
        if('\\x'==j):
            print('None')
print(s)
for i in s:
    print(is_hex(i))
    


# In[ ]:




