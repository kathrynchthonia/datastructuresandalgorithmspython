# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:38:17 2019

@author: tony
"""

#tuple unpacking
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
fib(7)


#

def rec_fib(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

fib(10)


def memoize(fn,arg):
    memo = {}
    if arg not in memo:
        memo[arg] = fn(arg)
    return memo[arg]

memoize(fib,7)