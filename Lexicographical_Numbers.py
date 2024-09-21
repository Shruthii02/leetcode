#!/usr/bin/env python
# coding: utf-8

# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Input: n = 2
# Output: [1,2]

# In[ ]:


n = int(input("Enter integer n : "))
def lexicalorder(n):
    nums = list(map(str,range(1,n+1)))
    nums.sort()
    rslt = list(map(int,nums))
    return rslt
print("Output ",lexicalorder(n))


# In[ ]:




