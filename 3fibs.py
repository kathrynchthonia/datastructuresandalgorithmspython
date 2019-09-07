# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:45:28 2019

@author: tony
"""
#recursive fib O^2
def rec_fib(n):
    if n <= 1:
        return n
    return rec_fib(n-1)+rec_fib(n-2)

rec_fib(4)

n = 10
memo = [None]*(n+1)
#Dynamic Fib
def memo_fib(n):
    #base case
    if n <= 1:
        return n
    # check cache
    else:
        if memo[n] != None:
            return memo[n]
        #set cache
        else:
            memo[n] = memo_fib(n-1) + memo_fib(n-2)
            return memo[n]
        
      
memo_fib(4)
#iterative fib
def iter_fib(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a+b
        
    return a

iter_fib(10)