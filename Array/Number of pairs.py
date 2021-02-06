# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:45:34 2021

@author: ayush
"""
# simple
"""
a=[2,3,4,5]
b=[1,2,3]
c=0
for x in a:
    for y in b:
        if x**y>y**x:
            c+=1
print(c)
"""
# Optimize
a=[2,3,4,5]
b=[1,2,3]
n=3
m=4
c,z,o,tw,t,f=0,0,0,0,0,0
def ind(b,n,v):
    l=0
    h=n-1
    c=-1
    while(l<=h):
        mid= int((l+h)/2)
        if b[mid]>v:
            c=mid
            h = mid-1
        else:
            l = mid+1
    return c
a=sorted(a)
b=sorted(b)
for i in b:
    if i==0:
        z+=1
    if i==1:
        o+=1
    if i==2:
        tw+=1
    if i==3:
        t+=1
    if i==4:
        f+=1
        
for x in range(m):
    if a[x]==0:
        continue
    elif a[x]==1:
        c+=z
    elif a[x]==2:
        i= ind(b,n,a[x])
        if i!=-1:
            c += n-i
        c -= t
        c -= f
        c+= o+z
    else:
        i= ind(b,n,a[x])
        if i!=-1:
            c+=n-i
        c+= o+z
        if a[x]==3:
            c+=tw
print(c)