#!/usr/bin/env python
# coding: utf-8

# # Count characters occurrences using Python

# In[6]:


def count_characters(s):
    count={}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i]=1
    print(count)
word=input("Enter your string:")
print(count_characters(word))


# In[ ]:




