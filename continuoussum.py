# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:00:57 2019

@author: tony
"""

def large_cont_sum(arr):
    if len(arr) < 1:
        return 0
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        max_sum = max(current_sum,max_sum)
        
    return max_sum

        


large_cont_sum([1,2,-1,3,4,10,10,-10,-1])

large_cont_sum([1,2,3,4,10,10,-10,-1])

