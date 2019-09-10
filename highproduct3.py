# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 20:00:37 2019

@author: tony
"""

def high_prod(lst):
    high = max(lst[0],lst[1])
    low = min(lst[0],lst[1])
    
    high_prod2 = lst[0]*lst[1]
    low_prod2 = lst[0]*lst[1]
    
    high_prod2 = lst[0]*lst[1]*lst[2]
    
    for num in lst[2:]:
        high_prod3 = max(high_prod3, num*high_prod2,num*low_prod2)
        
        high_prod2= max(high_prod2,num*high,num*low)
        
        low_prod2= min(low_prod2,num*high,num*low)
        
        high = max(high,num)
        low = min(low,num)
        
    return high_prod3