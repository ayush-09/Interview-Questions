# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:51:27 2021

@author: ayush
"""

class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    if image == None or image[sr][sc]== newColor:
	        return image
	    self.fill(image,sr,sc,image[sr][sc], newColor)
	    return image
	def fill(self,image,r,c,initial,newColor):
	    if r<0 or r>= len(image) or c<0 or c>= len(image[0]) or image[r][c] != initial:
	        return
	    image[r][c]=newColor
	    self.fill(image,r+1,c,initial,newColor)#down
	    self.fill(image,r-1,c,initial,newColor)#up
	    self.fill(image,r,c+1,initial,newColor)#right
	    self.fill(image,r,c-1,initial,newColor)#left

if __name__=="__main__":
    T=int(input())
    for i in range(T):
        n,m=input().split()
        n=int(n)
        m=int(m)
        image=[]
        for _ in range(n):
            image.append(list(map(int,input().split())))
        sr,sc,newColor=input().split()
        sr = int(sr)
        sc=int(sc)
        newColor = int(newColor)
        obj=Solution()
        ans=obj.floodFill(image, sr, sc, newColor)
        for _ in ans:
            for __ in _:
                print(__,end=" ")
            print()
            