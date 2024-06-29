#!/usr/bin/env python
# coding: utf-8

# You are given an array prices where prices[i] is the price of a given stock on the ith day.You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Input: prices = [7,6,4,3,1]
# Output: 0

# In[ ]:


arr = input("Enter the array: ")
prices = [int(item) for item in arr.split(",")]

def stock(prices):
    left , right = 0,1
    profit = 0
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = max(profit,prices[right] - prices[left])
        else:
            left = right
        right +=1
    return profit
print ("output",stock(prices))


# In[ ]:





# In[ ]:




