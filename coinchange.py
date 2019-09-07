# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:26:32 2019

@author: tony
"""

def rec_coins(target,coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        #for every coin val that is <= target val
        for i in [c for c in coins if c<= target]:
            #add coin count + recursive
            num_coins = 1 + rec_coins(target-i,coins)
            #reset minimum if new mumber of coins is less than min coins
            if num_coins < min_coins:
                min_coins = num_coins
        
    return min_coins

coins = [1,5,10,25]

rec_coins(15,coins)


# dynamic solution
def dyn_coin(target,coins,known):
    #Default output to target
    min_coins = target
    
    #base_case
    if target in coins:
        known[target] = 1
        return 1
    #Return known
    elif known[target]>0:
        return known[target]
    else:
        #for every coin that is less than target
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + dyn_coin(target-i,coins,known)
            
            if num_coins < min_coins:
                min_coins = num_coins
                #reset
                known[target] = min_coins
                
    return min_coins

coins = [1,5,10,25]
target = 74

known = [0]*(target+1)

dyn_coin(target,coins,known)
                

        
        