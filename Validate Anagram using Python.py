#!/usr/bin/env python
# coding: utf-8

# # Validate Anagram using Python

# In[3]:


def anagram(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    return sorted(word1)==sorted(word2)
print(anagram("cinema","iceman"))
print(anagram("cool","loco"))
print(anagram("men","women"))


# In[ ]:




