# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:19:24 2019

@author: tony
"""

def reverse(s):
    # Base case
    if len(s) <=1:
        return s
    #recursion
    return reverse(s[1:]) + s[0]

reverse('four')