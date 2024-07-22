#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


input_str = input("Enter the matrix: ")
grid = eval(input_str)
def numIsland(grid):
    def dfs(grid,r,c):
        grid [r][c] = '0'
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        for dr,dc in direction:
            nc,nr = dc+c,dr+r
            
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == '1':
                dfs(grid,nr,nc)
    count = 0
    for r in range  (len(grid)):
        for c in range (len(grid[0])):
            if grid[r][c] == '1':
                count += 1
                dfs(grid,r,c)
    return count 
print("Output",numIsland(grid))


# In[ ]:




