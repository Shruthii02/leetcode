#!/usr/bin/env python
# coding: utf-8

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]

# In[ ]:


interval = input("Enter the intervals ")
intervals = eval(interval)
def mergeIntervals(intervals):
    intervals.sort()
    merged = []
    for i in intervals:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else :
            merged[-1][1] = max(merged[-1][1],i[1])
    return merged
print( "Output ",mergeIntervals(intervals))            


# In[ ]:




