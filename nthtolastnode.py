# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 06:49:40 2019

@author: tony
"""

class Node(object):
    def __init__(self,val):
        self.val= val
        self.nextnode=None
        
def nthToLastNode(n, node):
    length = 0
    cnode= node
    while cnode.nextnode:
        length += 1
        cnode = cnode.nextnode
    if (n-1)>length:
        raise LookupError('Error:  length longer than list...')
    
    i = 0
    nthnode = node

    while i <= (length-n):
        nthnode =  nthnode.nextnode
        i += 1
    return nthnode.val

a = Node(6)
b = Node(5)
c = Node(4)
d = Node(3)
e = Node(2)
f = Node(1)
a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e
e.nextnode=f

nthToLastNode(4,a)

#Solution 2
def nth_to_last_node(n,head):
    left = head
    right = head
    for i in range(n-1):
        if not right.nextnode:
            raise LookupError('Error: n is larger than the linked list')
        right = right.nextnode
    while right.nextnode:
        left = left.nextnode
        right = right.nextnode
        
    return left.val

a = Node(6)
b = Node(5)
c = Node(4)
d = Node(3)
e = Node(2)
f = Node(1)
a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e
e.nextnode=f

nth_to_last_node(6,a)
            

    