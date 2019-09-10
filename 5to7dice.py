# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:13:33 2019

@author: tony
"""

from random import randint

def convert5to7():
    output = 10
    while output > 7:
        output = randint(1,5)+randint(1,5) -1
        print('2 D5s produced a roll of: ',output)
    print('Your final roll is below:')
    return output

convert5to7()