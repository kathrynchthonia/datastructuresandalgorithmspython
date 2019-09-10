# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 20:10:27 2019

@author: tony
"""


def coin_change(n, coins):
    arr = [1] + [0]*n
    
    for coin in coins:
        for i in range(coin,n+1):
            arr[i] += arr[i-coin]
            
    if n == 0:
        return 0
    else:
        #numbers of ways to make change
        return arr[n]
    
c=[1,5,10,25]
coin_change(15,c)