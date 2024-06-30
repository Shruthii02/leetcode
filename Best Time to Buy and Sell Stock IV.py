#!/usr/bin/env python
# coding: utf-8

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7

# In[2]:


arr = input("Enter the array: ")
prices = [int(item) for item in arr.split(",")]
k = int(input("Enter the number "))

def stock(k, prices):
    n = len(prices)

    
    if k >= n // 2:
        max_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
    
    buy = [-float('inf')] * (k + 1)
    sell = [0] * (k + 1)
    
    for price in prices:
        for j in range(1, k + 1):
            buy[j] = max(buy[j], sell[j - 1] - price)
            sell[j] = max(sell[j], buy[j] + price)
    
    return sell[j]
print ("output",stock(k,prices))


# In[ ]:




