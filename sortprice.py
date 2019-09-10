# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:56:21 2019

@author: tony
"""

def sort_price(unsorted_prices,max_price):
    prices_to_counts = [0]*(max_price+1)
    
    for price in unsorted_prices:
        prices_to_counts[price] += 1
    sorted_prices = []
    
    for price, count in enumerate(prices_to_counts):
        for time in range(count):
            sorted_prices.append(price)
    
    return sorted_prices

l = [1,10,3,4,2,6,11,8]

sort_price(l,11)