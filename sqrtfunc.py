# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:40:53 2019

@author: tony
"""
#can not return float
def solution(num):
    if num < 0:
        return ValueError
    if num == 1:
        return 1
    
    for k in range((num//2)+1):
        
        if k**2 == num:
            return k
        elif k**2 > num:
            return k -1
    return k

solution(5)


#accurate solution
def squareroot(num):
    return num**(1/2)

squareroot(5)


#refactored
def better_sol(num):
    if num <0:
        raise ValueError
        
    if num == 1:
        return 1
    
    low = 0
    high = (num//2)+1
    while low+1 < high:
        mid = low + (high-low)//2
        square = mid ** 2
        
        if square == num:
            return mid
        
        elif square < num:
            low = mid
        
        else:
            high = mid
    return low

better_sol(5)