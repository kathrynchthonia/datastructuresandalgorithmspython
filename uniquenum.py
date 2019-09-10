# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:50:26 2019

@author: tony
"""

def find_unique(id_list):
    
    unique_id = 0
    
    for i in id_list:
        print('This is the current id being checked: ',i)
        print('This is the current unique id: ', unique_id)
        print('this is the result of the XOR: ',(unique_id^i))
        unique_id ^= i
        
    return unique_id

find_unique([1,2,3,4,3,2,1])