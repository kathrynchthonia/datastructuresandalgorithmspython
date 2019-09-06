# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:38:39 2019

@author: tony
"""

def func_sum(n):
    if n//10 ==0:
        return n
    return n % 10 + func_sum(n//10)

func_sum(44)



