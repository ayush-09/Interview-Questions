# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:57:47 2021

@author: ayush
"""

# Sum formula

def MissingNumber(array,n):
    s= n*(n+1)//2
    s1=sum(array)
    m = s-s1
    return m

print(MissingNumber([1], 2))