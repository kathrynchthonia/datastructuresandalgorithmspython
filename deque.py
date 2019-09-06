# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:26:21 2019

@author: tony
"""

class Deque(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)
        
    def addRear(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        len(self.items)
        

d = Deque()

d.addFront('ninja')
d.addFront('night')
d.addRear('moonlight')

d.size()

print(d.removeFront() + ' ' + d.removeRear())

d.isEmpty()

d.removeFront()