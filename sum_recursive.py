# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:53:43 2026

@author: reina
"""

"""
A recursive sum function.
"""

def sum_recursive(x):
    """
    x: list[int]
    """
    if not x:
        return 0
    if len(x)==1:
        return x[0]
    return x[0]+sum_recursive(x[1:])

if __name__ == '__main__':
    x = [12,2,30,9]
    res=sum_recursive(x)
    print(res)