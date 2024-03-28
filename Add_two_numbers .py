#!/usr/bin/env python
# coding: utf-8

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# In[1]:


l1 = input("Enter the lst1: ")
l1 = list(map(int, l1.split(",")))
l2 = input("Enter the lst2: ")
l2 = list(map(int, l2.split(",")))
result = 0
result1 = 0
for i, digit in enumerate ((l1)):
    result += digit * (10**i)
for i, digit in enumerate ((l2)):
    result1 += digit * (10**i)
sum_ = result + result1
num = str(sum_)
num_lst = [int(char) for char in num]
num_lst.reverse()
print(num_lst)


# In[ ]:




