# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 01:12:41 2019

@author: tony
"""

def comp(lst):
    print(lst[0]) #o1
    midpoint = int(len(lst)/2) #O n/2
    #On/2
    for val in lst[:midpoint]:
        print(val)
        
    for x in range(10): #O10
        print('Hello World')
        
lst = [1,2,3,4]

comp(lst)

#O(1+n/2+10)

#O(n)
def matcher(lst,match):
    
    for item in lst:
        if item == match:
            return True
        
    return False

matcher(lst, 1) #O(1)

matcher(lst,11) #O(n)

def create_list(n):
    new_list = []
    
    for num in range(n):
        new_list.append('new')
        
    return new_list

create_list(4)

def printer(n):
    #time complexity O(n)
    for x in range(10):
        print('Ninja') #Space complexity O(1)
        
printer(10)