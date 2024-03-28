#!/usr/bin/env python
# coding: utf-8

# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Input: s = "bbbbb"
# Output: 1
# 

# In[ ]:


s = input("Enter the string:")
length = 0
start = 0
char_set = set()
for i in range(len(s) ):
    while s[i] in char_set:
        char_set.remove(s[start]) 
        start += 1 
    char_set.add(s[i])
    length = max(length, i - start + 1)
print(length)


# In[ ]:





# In[ ]:




