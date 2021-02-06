# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:20:18 2021

@author: ayush
"""
# Simple
A=[1,3,3,2,3]
N=5
for i in A:
    if A.count(i)>N/2:
        print(i)
        break
else:
    print(-1)
    
# Moore's Voting Algo

a=[1,3,2]
N=3
m=0
c=1
for i in range(1,len(a)):
    if a[m]==a[i]:
        c+=1
    else:
        c-=1
    if c==0:
        m=i
        c=1
c=0
for i in range(len(a)):
    if a[m]==a[i]:
        c+=1
if c>N/2:
    print(a[m])
else:
    print(-1)