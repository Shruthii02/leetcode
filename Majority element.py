#!/usr/bin/env python
# coding: utf-8

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# eg 1:
# Input: nums = [3,2,3]
# Output: 3
# eg 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# In[2]:


nums = input("enter the array: ")
def majorityelement(nums):
    first = nums[0]
    count = 1
    for i in nums[1:]:
        count += (1 if first == i else -1)
        if ~ count:
            first = i
            count = 1
    return (first)  
print("Majority element ",majorityelement(nums))


# In[ ]:




