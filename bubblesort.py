# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:32:52 2019

@author: tony
"""

def bubble_sort(arr):
    for n in list(range(len(arr)-1,0,-1)):
        print('This is the n: ',n)
        for k in range(n):
            print('This is the k index check: ',k)
            if arr[k] > arr[k+1]:
                #temp = arr[k]
                #arr[k] = arr[k+1]
                #arr[k+1] = temp
                arr[k],arr[k+1] = arr[k+1],arr[k]
    return arr
                
        
        
arr = [5,3,4,4]

bubble_sort(arr)
list(range(len(arr)-1,0,-1)):
    