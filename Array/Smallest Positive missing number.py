# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:20:23 2021

@author: ayush
"""
a=[0,-10,1,3,-20]
c=0
for i in range(len(a)):
    if i not in a:
        c=i
        break
if c==0:
    print(len(a)+1)
else:
    print(c)