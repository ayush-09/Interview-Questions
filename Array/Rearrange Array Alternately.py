# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:23:29 2021

@author: ayush
"""
# Simple solution
"""
arr=[1,2,3,4,5]
n=[]
i=0
j=len(arr)-1
while(j>=i):
    if j!=i:
        n.append(arr[j])
        j-=1
    n.append(arr[i])
    i+=1
print(n)
"""

# No extra space

arr=[1,2,3,4,5]
mini = 0
maxi= len(arr)-1
me= max(arr) + 1
for i in range(len(arr)):
    if i%2==0:
        arr[i] = arr[i]+ arr[maxi]%me*me
        maxi-=1
    else:
        arr[i] = arr[i]+ arr[mini]% me * me
        mini+=1
for i in range(len(arr)):
    arr[i]= arr[i]//me
print(arr) # alternate array

# for original array arr[i]% me 
 