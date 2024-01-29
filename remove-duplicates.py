#!/usr/bin/env python
# coding: utf-8

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# 
# Example 1:
# 
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
#  
# Example 2:
# 
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,,,,,_]

# In[ ]:


num = input("Enter the array :")
nums = [int(item) for item in num.split(",")]
def removeduplicates (nums):
    lst = list(set(nums))
    return lst
print("unique list ",removeduplicates (nums))
print(len(removeduplicates (nums)))


# In[30]:


num = input("Enter the array :")
nums = [int(item) for item in num.split(",")]
def removeduplicates (nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return nums[:j + 1]
lst = removeduplicates (nums)
print("unique list ",lst)
print(len(lst))


# In[ ]:




