#!/usr/bin/env python
# coding: utf-8

# Given two strings needle and haystack
#  return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Eg 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Eg 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# 

# In[7]:


needle = input("Enter the needle  : ")
haystack = input("Enter the haystack : ")
def FirstOccurrence (needle,haystack):
    if len(needle) == 0:
        return 0
    elif needle not in haystack:
        return -1
    else:
        return len(haystack.split(needle)[0])
print(FirstOccurrence (needle,haystack))


# In[ ]:





# In[ ]:




