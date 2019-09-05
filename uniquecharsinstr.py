# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:27:04 2019

@author: tony
"""

def uni_char(s):
    return len(set(s)) == len(s)

uni_char('abcdefa')

def uni_char2(s):

    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True

uni_char2('abcdef')