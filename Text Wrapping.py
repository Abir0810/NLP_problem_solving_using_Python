#!/usr/bin/env python
# coding: utf-8

# # Text wrapping in Python

# In[9]:


import textwrap
value=""" I love
country and my 
ountry name is 
Bangladesh"""
wrapper=textwrap.TextWrapper(width=60)
word_list=wrapper.wrap(text=value)
for element in word_list:
    print(element)


# In[ ]:




