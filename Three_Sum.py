#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Input: nums = [0,1,1]
Output: []
Input: nums = [0,0,0]
Output: [[0,0,0]]
 


# In[ ]:


arr = input("Enter the array")
nums = [int(item) for item in arr.split(",")]
def threesum(nums):
    nums.sort()
    triplets = set()
    for i in range(len(nums) - 2):
        firstNum = nums[i]
        j = i + 1
        k = len(nums) - 1
        while j < k:
            secondNum  = nums[j]
            thirdNum = nums[k]

            potentialSum = firstNum + secondNum + thirdNum 
            if potentialSum > 0:
                k -= 1
            elif potentialSum < 0:
                j += 1
            else:
                triplets.add((firstNum , secondNum ,thirdNum))
                j += 1
                k -= 1
    return triplets
print("Output",threesum(nums))


# In[ ]:





# In[ ]:





# In[ ]:




