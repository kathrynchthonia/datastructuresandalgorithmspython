# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 05:52:59 2019

@author: tony
"""
class Node(object):
    def __init__(self,val):
        self.val= val
        self.nextnode=None
        
def reverse(head):
    current = head
    previous = None
    nextnode = None
    
    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode
        
    return previous

a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode=b
b.nextnode=c

print(a.nextnode.val)
print(b.nextnode.val)

reverse(a)

print(b.nextnode.val)
print(c.nextnode.val)

    
    