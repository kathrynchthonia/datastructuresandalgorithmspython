# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:59:52 2019

@author: tony
"""

memo = {}
def factorial(n):
    if n < 2:
        return 1
    if not n in memo:
        memo[n] = n * factorial(n-1)
        
    return memo[n]

factorial(10)

memo[10]