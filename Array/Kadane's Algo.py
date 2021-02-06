# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:28:46 2021

@author: ayush
"""
nums=[1,2,3,-2,5]
size=5
def maxSubArraySum(nums,size):
    max_c=m=nums[0]
    for i in range(1, size):
        max_c = max(nums[i],max_c+nums[i])
        if max_c>m:
            m=max_c
    return m
print(maxSubArraySum(nums, size))