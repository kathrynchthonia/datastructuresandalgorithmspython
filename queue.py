# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:28:03 2019

@author: tony
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
q = Queue()
q.size()

q.isEmpty()   

q.enqueue(4)
q.enqueue('fourier')
q.dequeue()