#!/usr/bin/env python
# coding: utf-8

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false 

# In[ ]:


def courseschedule(numCourses, prerequisites):
    numCourses = int(numCourses)
    
    prerequisites = eval(prerequisites)
    
    graph = [[] for _ in range(numCourses)]
    visited = [0] * numCourses
    
    for c1, c2 in prerequisites:
        graph[c2].append(c1)
    
    def dfs(course):
        if visited[course] == 1:  
            
            return False
        if visited[course] == 2:  
            return True
        
        visited[course] = 1  
        
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        
        visited[course] = 2  
        return True
    
    for i in range(numCourses):
        if visited[i] == 0:  
            if not dfs(i):
                return False
    
    return True

numCourses = input("Enter the number of courses: ")
prerequisites = input("Enter the prerequisites : ")

print("Output:", courseschedule(numCourses, prerequisites))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




