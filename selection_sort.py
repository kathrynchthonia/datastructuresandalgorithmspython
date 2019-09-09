# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:58:31 2019

@author: tony
"""

def selection_sort(arr):
    
    for fillslot in list(range(len(arr)-1,0,-1)):
        positionOfMax = 0
        
        for location in list(range(1,fillslot+1)):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location
                

        arr[fillslot],arr[positionOfMax] = arr[positionOfMax],arr[fillslot]
    return arr
        
        
arr = [5,3,4,4] 
selection_sort(arr)   