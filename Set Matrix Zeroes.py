#!/usr/bin/env python
# coding: utf-8

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]] 
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]   

# In[6]:


matrix = (input("Enter the matrix "))
matrix = eval(matrix)
def setMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    z_row = [False] * m
    z_col = [False] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                z_row[i] = True
                z_col[j] = True
    for i in range(m):
        for j in range(n):
            if z_row[i] or z_col[j] :
                matrix[i][j] = 0
    return matrix
print(setMatrix(matrix))
            


# In[ ]:




