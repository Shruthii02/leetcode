#!/usr/bin/env python
# coding: utf-8

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# In[ ]:


arr = input("Enter the array ")
nums = [int(item) for item in arr.split(",")]
def longestConsecutive(nums):
    num_set = set(nums)
    count = 0
    for num in num_set:
        if num-1 not in num_set:
            current_num = num
            pre_count = 1
            while current_num+1 in num_set:
                current_num+=1
                pre_count +=1
            count = max(pre_count,count)
    return count
print("output",longestConsecutive(nums))


# In[ ]:




