# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 01:44:18 2019

@author: tony
"""

def method1():
    l = []
    for n in range(10000):
        l = l + [n]
        
def method2():
    l = []
    for n in range(10000):
        l.append(n)
def method3():
    l = [n for n in range(10000)]
    
def method4():
    l = list(range(10000))
    
    
%timeit method1()
%timeit method2()
%timeit method3()
%timeit method4()


d = {'k1':1, 'k2':2}

d['k1']