#!/usr/bin/env python
# coding: utf-8

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Input: heights = [[1]]
# Output: [[0,0]]

# In[ ]:


def pacificAtlantic(matrix):
    matrix = eval(matrix)
    m,n = len(matrix),len(matrix[0])
    p = [[False] * n for _ in range(m)]
    a = [[False] * n for _ in range(m)]

    def dfs (x,y,ocean):
        ocean[x][y] =  True
        for dx,dy in  [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and not ocean[nx][ny] and matrix[nx][ny] >= matrix[x][y]:
                dfs(nx,ny,ocean)
    for i in range(m):
        dfs(i,0,p)
        dfs(i,n-1,a)
    for j in range(n):
        dfs(0,j,p)
        dfs(m-1,j,a)
    result = []
    for i in range(m):
        for j in range(n):
            if p[i][j] and a[i][j]:
                result.append([i,j])
    return result
matrix = input("Enter the heights : ")

print("Output",pacificAtlantic(matrix))


# In[ ]:





# In[ ]:




