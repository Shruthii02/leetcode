#!/usr/bin/env python
# coding: utf-8

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# eg:Input: prices = [7,1,5,3,6,4]
# Output: 5

# In[10]:


price = input("enter the array: ")
prices = [int(item) for item in price.split(",")]
def stockprofit(price):
    first_price = price[0]
    profit = 0
    for i in range(1,len(price)):
        if(price[i]<first_price):
            first_price = price[i]
        else:
            profit = max(profit, price[i] - first_price)
    return profit
print("Maximum profit ",stockprofit(prices))


# 

# In[29]:





# In[23]:





# In[ ]:




