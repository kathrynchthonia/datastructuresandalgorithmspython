# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:34:55 2019

@author: tony
"""

def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                
                i+= 1
                
            else:
                arr[k] = righthalf[j]
                j+= 1
            k+= 1
            
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
            
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j+=1
            k+=1
        print('Merging: ',arr)
    return arr

arr = [5,3,4,4,0,1,3,2,7,5,6] 
merge_sort(arr)
            
        