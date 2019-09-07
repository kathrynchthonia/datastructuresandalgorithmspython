# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:27:26 2019

@author: tony
"""

def permute(s):
    out = []
    
    if len(s) == 1:
        out = [s]
        
    else:
        #for every letter in string
        for i,let in enumerate(s):
            #for every permutation resulting from step 2 and 3
            for perm in permute(s[:i] + s[i+1:]):
                #add it to the output
                print('perm is ', perm)
                out += [let+perm]
    return out

permute('cat')