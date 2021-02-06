# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:07:16 2021

@author: ayush
"""
def t(arr,n): 
    p=0
    tp=0
    for i in range(n):
       pt = arr[i] * p
       p= p + 1
       tp += pt
    return tp
print(t([1,2,2,4,9],5))