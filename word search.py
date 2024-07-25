#!/usr/bin/env python
# coding: utf-8

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# In[9]:


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

def search (board,word):
    def track(i,j,k):
        if k ==  len(word):
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[k]:
            return False
        temp = board[i][j]
        board[i][j] = ''
        if track(i+1,j,k+1) or track(i-1,j,k+1) or track(i,j+1,k+1) or track(i,j-1,k+1):
            return True
        board[i][j] = temp
    for i in range(len(board)):
        for j in range(len(board[0])):
            if track(i,j,0):
                return True
    return False
            
print(search (board,word))

