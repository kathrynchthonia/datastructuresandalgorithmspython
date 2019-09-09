# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:55:48 2019

@author: tony
"""

prices = [12,11,15,3,10]

def profit(stock_prices):
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices...')
    min_stock_price = stock_prices[0]
    
    max_profit = 0
    
    for price in stock_prices:
        min_stock_price = min(min_stock_price,price)
        
        comparison_profit = price - min_stock_price
        
        max_profit = max(max_profit,comparison_profit)
        
    return max_profit

profit(prices)


#with edge cases
def profit2(stock_prices):
    #check length
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices...')
        #start minimum price marker at first price
    min_stock_price = stock_prices[0]
    #start off with a max profit
    max_profit = stock_prices[1] - stock_prices[0]
    #skip index 0
    for price in stock_prices[1:]:
        #check price against min for profit
        #compare against mi profit
        comparison_profit = price - min_stock_price
        #compare against max profit so far
        max_profit = max(max_profit,comparison_profit)
        #Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price,price)
        
    return max_profit

prices = ([1])
profit2(prices)

prices = ([30,22,21,15])
profit2(prices)
