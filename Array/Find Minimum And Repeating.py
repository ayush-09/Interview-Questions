# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:01:42 2021

@author: ayush
"""

a=[1,3,3]
r=set()
re=0
for i in range(len(a)):
    if i not in a and i<a[i]:
        m=i
    if a[i] not in r:
        r.add(a[i])
    else:
        re=a[i]

print(re,m)