# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:24:41 2019

@author: tony
"""

def shell_sort(arr):
    sublistcount = len(arr)//2
    
    while sublistcount > 0:
        for start in range(sublistcount):
            
            gap_insertion_sort(arr,start,sublistcount)
        print('After increments of size: ',sublistcount)
        print('The list is: ',arr)
        sublistcount = sublistcount//2
    return arr
        
def gap_insertion_sort(arr,start,gap):
    
    for i in range(start+gap,len(arr),gap):
        
        currentValue = arr[i]
        position = i
        
        while position >= gap and arr[position-gap] > currentValue:
            arr[position] = arr[position-gap]
            position = position-gap
            
        arr[position] = currentValue
        
arr = [5,3,4,4,0,1,3,2,7,5,6] 
shell_sort(arr) 