# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 05:33:02 2019

@author: tony
"""

def seq_search(arr,ele):
    pos = 0
    found = False
    while pos< len(arr) and not found:
        
        if arr[pos] == ele:
            found = True
            
        else:
            pos += 1
            
    return found

arr = [1,2,3,4,5,6]
seq_search(arr,4)


def ordered_seq_search(arr,ele):
    pos = 0
    found = False
    stopped = False
    while pos< len(arr) and not found and not stopped:
        
        if arr[pos] == ele:
            found = True
            
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1
            
            
    return found

arr = [1,2,3,5,5,6]
ordered_seq_search(arr,4)


#refactored
def ordered_seq_search2(arr,ele):
    pos = 0
    found = False
    while pos< len(arr) and not found:
        
        if arr[pos] == ele:
            found = True
            
        else:
            if arr[pos] > ele:
                return False
            else:
                pos += 1
            
            
    return found

arr = [1,2,3,5,5,6]
ordered_seq_search2(arr,4)