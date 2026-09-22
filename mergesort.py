# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:34:49 2026

@author: reina
"""

def mergesort(x):
    if len(x)<=1:
        return x
    else:
        l,r=0,len(x)-1
        mid=l+(r-l+1)//2
        # mid=len(x)//2
        left=mergesort(x[:mid])
        right=mergesort(x[mid:])
        #merge
        res=[]
        i,j=0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if i<len(left):
            res.extend(left[i:])
        if j<len(right):
            res.extend(right[j:])
        return res
        
        
if __name__ == '__main__':
    x=[1,11,3,5,-1,13,2]
    # x=[1,-2]
    # x=[1]
    # x=[1,11]
    res=mergesort(x)
    print(res)