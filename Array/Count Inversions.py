# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:56:48 2021

@author: ayush
"""
# Brute force
"""
a=[2,3,4,5,6]
c=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            c+=1
print(c)
"""
# Merge sort
def merge(arr,temp,left,mid,right):
    c=0
    i=left
    j=mid
    k=right
    while((i<=mid-1) and (j<=right)):
        if arr[i]<=arr[j]:
            
def mergeSort(arr,temp,left,right):
    mid,c=0,0
    if right>left:
        mid = (right+left)//2
        c+= mergeSort(arr, temp, left, mid)
        c+= mergeSort(arr, temp, mid+1, right)
        c+= merge(arr,temp,left,mid+1,right)
    return c

        