# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 12:45:12 2021

@author: ayush
"""

a=[1,2,3,4,5,6,7,8]
k=5
for i in range(0,len(a),k):
    s = i
    e = min(i+k-1, len(a)-1)
    print(e)
    while(s<=e):
        t=a[s]
        a[s] = a[e]
        a[e]=t
        s+=1
        e-=1
print(a)
    