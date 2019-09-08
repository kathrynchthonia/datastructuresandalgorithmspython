# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:43:07 2019

@author: tony
"""

def binary_search(arr,ele):
    first = 0
    last = len(arr)-1
    i = None
    found = False
    
    while first <= last and not found:
        mid = (first+last)//2
        if arr[mid] == ele:
            found = True
            i = mid
        elif ele < arr[mid]:
            last = mid-1
        else:
            first = mid+1
    return found

arr = [1,2,3,5,5,6]

binary_search(arr, 2)


def rec_bin_search(arr,ele):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if arr[mid] == ele:
            return True
        elif ele < arr[mid]:
            return rec_bin_search(arr[:mid],ele)
        else:
            return rec_bin_search(arr[mid+1:],ele)
        
    
arr = [1,2,3,5,5,6]

rec_bin_search(arr, 4)
        