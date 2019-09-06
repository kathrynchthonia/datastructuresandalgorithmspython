# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:27:25 2019

@author: tony
"""

def rec_sum(n):
    if n == 0:
        return 0
    if n < 0:
        return n + rec_sum(n+1)
    return n + rec_sum(n-1)

rec_sum(4)
rec_sum(-4)