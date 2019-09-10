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


#alternate version
def d5():
    return randint(1,5)

def convert5to7():
    while True:
        
        roll_1 = d5()
        roll_2 = d5()
    
        num = ((roll_1-1)*5)+(roll_2)
    
        if num > 21:
            continue
    
        return num%7 + 1

convert5to7()
