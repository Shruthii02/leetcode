#!/usr/bin/env python
# coding: utf-8

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Input: nums = [1,2,3,1]
# Output: true
# Input: nums = [1,2,3,4]
# Output: false
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# In[ ]:


arr = input("Enter the array")
nums = [int(item) for item in arr.split(",")]
def ContainsDuplicate(nums):
    initial = set()
    for i in nums:
        if i in initial :
            return True
        else:
            initial.add(i)
    return False
print("output",ContainsDuplicate(nums))
            


# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#  

# In[2]:


arr = input("Enter the array")
nums = [int(item) for item in arr.split(",")]
k = int(input("Enter the number"))
def ContainsDuplicate(nums,k):
    hset = {}
    for i in range(len(nums)):
        if nums[i] in hset and abs(i - hset[nums[i]]) <= k :
            return True
        hset[nums[i]] =  i 
    return False
            
print("Output",ContainsDuplicate(nums,k))

