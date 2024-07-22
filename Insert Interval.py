#!/usr/bin/env python
# coding: utf-8

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]] 

# In[8]:


interval = input("Enter the intervals ")
intervals = eval(interval)
newIntervals = input("Enter the newInterval ")
new_intervals = eval(newIntervals)
def InsertInterval(intervals,new_intervals):
    res = []
    n = len(intervals)

    for i in range(n):
        start , end = intervals[i]
        if new_intervals[0]>end:
            res.append(intervals[i])
        elif new_intervals[1]<start:
            res.append(new_intervals)
            return res + intervals[i:]
        else:
            new_intervals[0] = min(start,new_intervals[0])
            new_intervals[1] = max(end,new_intervals[1])
    res.append(new_intervals)
    return res
print(InsertInterval(intervals,new_intervals))


    


# In[ ]:





# In[ ]:




