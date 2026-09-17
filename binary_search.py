# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:14:48 2026

@author: reina
"""

def binary_search(x,target):
    l,r=0,len(x)-1
    def helper(l,r):
        if l<r:
            mid=l+(r-l+1)//2
            print(l,mid,r)
            if x[mid]==target:
                return mid
            if target<x[mid]:
                return helper(l,mid-1)
            else:
                return helper(mid,r)
        else:
            return -1
    return helper(l,r)    
    

if __name__ == '__main__':
    x=[2,3,5,7,11,13]
    x=[2]
    target=11
    target=3
    res=binary_search(x,target)
    print(res)