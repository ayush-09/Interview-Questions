# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:23:50 2021

@author: ayush
"""

a=[20,17,42,25,32,32,30,32,37,9,2,33,31,17,14,40,9,12,36,21,8,33,6,6,10,37,12,26,21,3]

t=0
total=sum(a)
if len(a)==1:
    print(1)
for i in range(len(a)):
    total = total-a[i]
    if total==t:
        print(i+1)
    t+=a[i]
    