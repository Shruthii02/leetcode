#!/usr/bin/env python
# coding: utf-8

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.
# Eg 1:
# Input: ratings = [1,0,2]
# Output: 5
# Eg 2:
# Input: ratings = [1,2,2]
# Output: 4

# In[43]:


arr = input("Enter the array: ")
ratings= [int(item) for item in arr.split(",")]
def countCandies(ratings):
    n = len(ratings)
    candies = [1] * n 
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    return sum(candies)
print("minimum number of candies:",countCandies(ratings))


# In[ ]:




