# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:07:25 2019

@author: tony
"""

def pair_sum(arr,k):
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    for num in arr:
        target = k-num
        
        if target not in seen:
            seen.add(num)
            
        else:
            output.add( ((min(num, target)), max(num,target)))
            
    #return len(output)

    print( '\n'.join(map(str,list(output))))

arr= [1,3,2,2,4]

pair_sum(arr,4)