# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 03:22:24 2019

@author: tony
"""

class Node(object):
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

a.value
b.nextnode.value