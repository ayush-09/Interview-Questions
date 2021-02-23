# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 21:29:19 2021

@author: ayush
"""
# Brute Force
"""
a=[1,60,-10,70,-80,85]
s=a[0]+a[1]
l=0
r=1
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        c=a[i]+a[j]
        if abs(s)>abs(c):
            s=c
            l=i
            r=j
print(a[l],a[r])
"""

# Sorting
import sys
a=[-21,-67,-37,-18,4,-65]
a=sorted(a)
ml=1
mr=len(a)-1
l=0
r=len(a)-1
ms=sys.maxsize
while l<r:
    s=a[l]+a[r]
    if abs(s)<abs(ms):
        ms=s
        ml=l
        mr=r
    if s<0:
        l+=1
    else:
        r-=1
print(a[ml]+a[mr])