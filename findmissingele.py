# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:24:18 2019

@author: tony
"""

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
        
    return arr1[-1]

arr1 =[1,2,3,4,5,6,7]
arr2 = [2,4,6,1,5,7]
finder(arr1,arr2)

#Finder 2 
import collections
def finder2(arr1,arr2):
    d = collections.defaultdict(int)
    
    for num in arr2:
        d[num] += 1
        
    for num in arr1:
        if d[num] == 0:
            return num
        
    else:
        d[num] -= 1
        
finder2(arr1,arr2)

#linear time constant space
def finder3(arr1,arr2):
    result=0
    
    #Perform an XOR between the numbers in the arrays
    for num in arr1+arr2:
        result^=num
        print result
        
    return result

finder3(arr1,arr2)