#!/usr/bin/env python
# coding: utf-8

# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# Input: a = 1, b = 2
# Output: 3
# Input: a = 2, b = 3
# Output: 5

# In[ ]:


a = int(input("Enter a "))
b = int(input("Enter b "))

def getsum(a,b):
    if b == 0:
        return a
    elif b>0:
        while b>0:
            b-=1
            a+=1
    else :
        while b<0:
            b+=1
            a-=1
    return a
print("Output",getsum(a,b))


# Write a function that takes the binary representation of a positive integer and returns the number of 
# set bits
# Input: n = 11
# Output: 3
# Input: n = 128
# Output: 1
# Input: n = 2147483645
# Output: 30

# In[ ]:


n = int(input ("Enter the number "))
def onebit(n):
    binary = bin(n)
    s = binary.split("1")
    res = len(s) - 1
    return res
print("Output ",onebit(n))


# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Input: n = 2
# Output: [0,1,1]
# Input: n = 5
# Output: [0,1,1,2,1,2]

# In[ ]:


n = int(input ("Enter the number "))
def countbits(n):
    count = []
    for j in range (0,n+1):
        binary = bin(j)
        s=binary.split("1")
        res = len(s) - 1
        count.append(res)
    return count
print("Output",countbits(n))


# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array 
# Input: nums = [3,0,1]
# Output: 2
# Input: nums = [0,1]
# Output: 2
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8 

# In[ ]:


arr = input("Enter the arr ")
nums = [int(item) for item in arr.split(",")]
def missingNumber(nums):
    n = len(nums)
    for i in range(0,n+1):
        if (i not in nums):
            return i
print("output",missingNumber(nums))


# Reverse bits of a given 32 bits unsigned integer.
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)

# In[22]:


def reverse_bits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
n1 = 0b00000010100101000001111010011100
print("Output",reverse_bits(n1))  
n2 = 0b11111111111111111111111111111101
print("Output",reverse_bits(n2))  

