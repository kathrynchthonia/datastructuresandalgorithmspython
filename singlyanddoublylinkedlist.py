# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 07:39:16 2019

@author: tony
"""

class Snode(object):
    def __init__(self,val):
        self.val = val
        self.nextnode = None
        
class Dnode(object):
    def __init__(self,val):
        self.val = val
        self.nextnode = None
        self.lastnode = None
        
        
a = Snode(6)
b = Snode(5)
c = Snode(4)

a.nextnode=b
b.nextnode=c

a.nextnode.val
a.val

e=Dnode(4)
f=Dnode(44)
g=Dnode(444)

e.nextnode=f
f.nextnode=g
f.lastnode=e
g.lastnode=f

g.lastnode.val
