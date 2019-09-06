# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:18:53 2019

@author: tony
"""

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return n * factorial(n+1)
    
    return n * factorial(n-1)

factorial(4)
factorial(-4)