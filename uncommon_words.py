#!/usr/bin/env python
# coding: utf-8

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
# 

# In[19]:


s1 = str(input("Enter the string 1 "))
s2 = str(input("Enter the string 2 "))
def UncommonWords(s1,s2):
    w1 = s1.split()
    w2 = s2.split()
    rslt = []
    words = w1+w2
    count = Counter(words)
    for i in words:
        if count[i] == 1:
            rslt.append(i)
    return rslt
print("Output",UncommonWords(s1,s2))


# In[18]:


s1 = str(input("Enter the string 1 "))
s2 = str(input("Enter the string 2 "))
def UncommonWords(s1,s2):
    w1 = s1.split()
    w2 = s2.split()
    rslt = []
    words = w1+w2
    count = {}
    for i in words:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in count :
        if count[i] == 1:
            rslt.append(i)
    return rslt
print("Output",UncommonWords(s1,s2))


# In[ ]:




