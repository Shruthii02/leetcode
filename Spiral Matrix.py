#!/usr/bin/env python
# coding: utf-8

# Given an m x n matrix, return all elements of the matrix in spiral order.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# In[ ]:


matrix = input("Enter the matrix ")
matrix = eval(matrix)
def spiralorder(matrix):
    n = len(matrix)-1
    m = len(matrix[0])-1
    row_s = 0
    col_s = 0
    res = []
    if len(matrix) == 0 :
        return res
    while row_s <= n and col_s <= m:
        for i in range(col_s,m+1):
            res.append(matrix[row_s][i])
        row_s += 1
        for i in range(row_s,n+1):
            res.append(matrix[i][m])
        m -= 1
        if row_s <= n :
            for i in range(m,col_s-1,-1):
                res.append(matrix[n][i])
            n-=1
        if col_s <= m:
            for i in range(n,row_s-1,-1):
                res.append(matrix[i][col_s])
            col_s +=1
    return res
print("Output",spiralorder(matrix))


# In[ ]:




