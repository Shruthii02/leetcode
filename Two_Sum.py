#!/usr/bin/env python
# coding: utf-8

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# In[6]:


arr = (input("Enter the array "))
nums = [int(item) for item in arr.split(",")]
target = int(input("Enter the target"))
def Two_sum(nums,target):
    heap = {}
    for i,num in enumerate(nums):
        if target - num in heap :
            return (i,heap[target - num])
        heap[num] = i
    return -1
print ("Output",Two_sum(nums,target))


# In[ ]:





# In[ ]:





# In[ ]:




