# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:33:00 2019

@author: tony
"""

def removeDups(s):
    result = []
    seen = set()
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

s='ninjaninja'
removeDups(s)