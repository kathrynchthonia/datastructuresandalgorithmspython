# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:42:11 2019

@author: tony
"""

from random import randint

def dice7():
    return randint(1,7)

def convert7to5():
    roll = 7
    
    while roll > 5:
        roll = dice7()
        print('D7 produced a roll of ', roll)
    print('Your final roll is bolow:')
    return roll

convert7to5()
