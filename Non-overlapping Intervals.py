#!/usr/bin/env python
# coding: utf-8

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Input: intervals = [[1,2],[2,3]]
# Output: 0

# In[ ]:


interval = input ("Enter the intervals ")
intervals = eval (interval)
def NonOverlapping(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    
    for i in range(1,len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    return count
print("Output" , NonOverlapping(intervals))

