# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 03:38:28 2019

@author: tony
"""

class Node(object):
    def __init__(self,val):
        self.val= val
        self.nextnode=None
        

def cycle_check(node):
    marker1 = node
    marker2 = node
    
    while marker2 !=None and marker2.nextnode != None:
        marker1=marker1.nextnode
        marker2=marker2.nextnode.nextnode
        
        if marker2 == marker1:
            return True
    return False

a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode=b
b.nextnode=c
c.nextnode=a

cycle_check(a)
c.nextnode=None
cycle_check(a)