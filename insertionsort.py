# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:05:25 2019

@author: tony
"""

def insertion_sort(arr):
    for i in list(range(1,len(arr))):
        currentValue = arr[i]
        position = i
        
        while position > 0 and arr[position-1]>currentValue:
            
            arr[position] = arr[position-1]
            position = position-1
            
        arr[position] = currentValue
    return arr

arr = [5,3,4,4] 
insertion_sort(arr) 


#insertionsort faster
def insertion_sort(arr):
    for i in range(1, len(arr)):
        position = i
        
        for j in range(i-1, -1, -1):
            if arr[j] > arr[position]:
                arr[j], arr[position] = arr[position], arr[j]
                position -= 1
            else:
                break
    return arr

arr = [5,3,4,4] 
insertion_sort(arr) 