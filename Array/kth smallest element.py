# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:25:29 2021

@author: ayush
"""

arr=[7,10,4,3,20,15]
n=len(arr)
k=3
def kthSmallest(arr, l, r, k):
    arr=sorted(arr)
    return arr[k-1]
print(kthSmallest(arr, 0,n-1, k))