# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:07:35 2021

@author: ayush
"""

def countStrings(n):
    a = 1
    b = 1
    for i in range(1,n):
        tmp = a
        a = a + b
        b = tmp
        #print(a)
        #print(b)
    return (a + b)%(10**9+7)
print(countStrings(4))