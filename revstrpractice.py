# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:37:29 2019

@author: tony
"""

def reverse(s):
    if len(s) <= 1:
        return s
    
    return reverse(s[1:]) + s[0]


s = 'wowowowoahwewoahwow'
reverse(s)
