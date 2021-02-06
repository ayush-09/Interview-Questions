# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:47:45 2021

@author: ayush
"""
n=5
s=12
arr=[1,2,3,7,5]
def subArraySum(arr, n, s): 
    c_s=0
    d={}
    for i in range(n):
        c_s = c_s + arr[i]
        if c_s == s:
            return 1,i+1
        if c_s-s in d:
            return d[c_s-s]+2,i+1
        d[c_s]=i
ans=subArraySum(arr, n, s)
for i in ans:
    print(i,end=" ")
print()