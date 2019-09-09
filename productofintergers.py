# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:10:10 2019

@author: tony
"""

def index_prod(lst):
    output = [None] * len(lst)
    
    product = 1
    i = 0
    
    while i < len(lst):
        output[i] = product
        
        product *= lst[i]
        
        i+= 1
    print('First forward pass: ',output)    
    product = 1
    i = len(lst) -1
    while i >= 0:
        output[i] *= product
        product *= lst[i]
        
        i-= 1
    return output
            
index_prod([1,2,3,4,5])
            