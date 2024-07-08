#!/usr/bin/env python
# coding: utf-8

# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Input: nums = [1]
# Output: 1
# Input: nums = [5,4,-1,7,8]
# Output: 23

# In[ ]:


arr = input("Enter the array: ")
nums = [int(item) for item in arr.split(",")]
def maxSubArray (nums):
    max_sum = nums[0]
    curr_sum = 0
    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sum = max(max_sum,curr_sum)
    return max_sum
print("output",maxSubArray(nums))
        


# #### Maximum Product Subarray
# Given an integer array nums, find a subarraythat has the largest product, and return the product.The test cases are generated so that the answer will fit in a 32-bit integer.
# Input: nums = [2,3,-2,4]
# Output: 6
# Input: nums = [-2,0,-1]
# Output: 0

# In[1]:


arr = input("Enter the array: ")
nums = [int(item) for item in arr.split(",")]
def maxProduct(nums):
    res = nums[0]
    cmax,cmin = 1,1
    for n in nums:
        cmax = max(cmax*n,cmin*n,n)
        cmin = min(cmax*n,cmin*n,n)
        res =  max(cmax,res)
    return res
print("Output",maxProduct(nums))


# In[ ]:




