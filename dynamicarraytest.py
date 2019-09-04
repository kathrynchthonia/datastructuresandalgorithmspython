# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 02:42:39 2019

@author: tony
"""
#Dynamic arrays test
import sys

# set n
n = 10

data = []

for i in range(n):
    #Number of elements
    a = len(data)
    
    #Actual size in bytes
    b = sys.getsizeof(data)
    
    print ('Length: {0:3d}; Size in Bytes: {1:4d} '.format(a,b))
    
    data.append(n)