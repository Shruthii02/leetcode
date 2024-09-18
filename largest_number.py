#!/usr/bin/env python
# coding: utf-8

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.
# Input: nums = [10,2]
# Output: "210"
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

# In[ ]:


num = (input("Enter the nums "))
nums = [int(item) for item in num.split(",")]
def largestnumber(nums):
    arr = list(map(str,nums))
    arr.sort(key = lambda x:x*10,reverse = True)
    if arr[0] == "0":
        return "0"
    largest = ''.join(arr)
    return largest
print("Output ",largestnumber(nums) )


# In[ ]:




