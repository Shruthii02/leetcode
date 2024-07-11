#!/usr/bin/env python
# coding: utf-8

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Input: height = [1,1]
# Output: 1

# In[ ]:


arr = input ("Enter the array ")
height = [int(item) for item in arr.split(",")]
def maxArea(height):
    maxarea = 0
    n = len(height)
    for i in range(n):
        for j in range(i+1,n):
            h = min(height[i],height[j])
            w = j-i
            area = h*w
            maxarea = max(maxarea,area)
    return maxarea 
print("Output",maxArea(height))


# In[ ]:




