# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:45:36 2019

@author: tony
"""

def sum_target(lst,target):
    seen = set()
    
    for num in lst:
        num2 = target - num
        
        if num2 in seen:
            return True
        
        seen.add(num)
        
    return False

l = [1,2,5,8,99,3,4,8,1,15]

sum_target(l,16)