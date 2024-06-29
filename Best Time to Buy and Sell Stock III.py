#!/usr/bin/env python
# coding: utf-8

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Input: prices = [1,2,3,4,5]
# Output: 4
# Input: prices = [7,6,4,3,1]
# Output: 0

# In[5]:


arr = input("enter the array ")
prices = [int(item) for item in arr.split(",")]
def stock(prices):
    if not prices:
        return 0
    buy1,buy2 = float('inf'),float('inf')
    sell1,sell2 =0,0
    for price in prices:
        buy1 = min(buy1,price)
        sell1 = max(sell1,price-buy1)
        buy2 = min (buy2,price-sell1)
        sell2 = max (sell2,price-buy2)
    return sell2
        
print("output",stock(prices))      


# In[ ]:





# In[ ]:




