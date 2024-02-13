#!/usr/bin/env python
# coding: utf-8

# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# Eg 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Eg 2:
# Input: s = "a", t = "a"
# Output: "a"
# 

# In[8]:


s = input("enter the string 'S' ")
t = input("enter the string 't' ")
from collections import Counter
def minWindow(s,t):
    s_count, t_count = Counter(), Counter(t)
    l = 0
    results = ""

    for r in range(len(s)):
        s_count[s[r]] += 1
        while all(s_count[char] >= count for char, count in t_count.items()):
            if len(s[l:r + 1]) < len(results) or not results:
                results = s[l:r + 1]
            s_count[s[l]] -= 1
            l += 1

    return results
print("Output",minWindow(s,t))

