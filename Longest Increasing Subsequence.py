#!/usr/bin/env python
# coding: utf-8

# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 

# In[ ]:


arr = input("Enter the numbers ")
nums = [int(item) for item in arr.split(",")]

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        
        for j in range(i):
            if nums[i] > nums[j] :
                dp[i] =  max(dp[i],dp[j]+1)
    return max(dp)
print("Output",lengthOfLIS(nums))


# In[ ]:




