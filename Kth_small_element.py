#!/usr/bin/env python
# coding: utf-8

# Given an array arr[] of size N and a number K, where K is smaller than the size of the array. Find the K'th smallest element in the given array.
# Given that all array elements are distinct.
# Eg:
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
# Output: 7
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
# Output: 10

# In[14]:


array = input("Enter the array:")
arr = [int(item) for item in array.split(",")]
k = int(input("Enter k:"))
def kth_smallest_element(arr, k):
    for i in range(0,k-1):
        small_element = min(arr)
        arr.remove(small_element)
    return min(arr)
result = kth_smallest_element(arr, k)
print("Output:", result)  


# In[ ]:




