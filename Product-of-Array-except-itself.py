#!/usr/bin/env python
# coding: utf-8

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.You must write an algorithm that runs in O(n) time and without using the division operation.
# Eg1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Eg2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#  

# In[7]:


arr = (input("Enter the array "))
nums = [int(item) for item in arr.split(",")]
def product_of_array (nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    product = [0] * n
    for i in range (1,n):
        left[i] = left[i-1] * nums [i-1]
    for i in range (n-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
    for i in range (n):
        product [i] = left[i] * right[i]
    return product
print("Output:", product_of_array (nums))       


# In[ ]:




