# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:48:16 2021

@author: ayush
"""

a=[15,18,5,3,6,2]
m=-1
for i in range(len(a)-1,0,-1):
    if a[i]>m:
        m=a[i]
        print(m,end=" ")

