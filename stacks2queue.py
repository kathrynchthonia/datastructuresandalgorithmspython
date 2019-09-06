# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 02:44:30 2019

@author: tony
"""

class Queue2Stacks(object):
    def __init__(self):
        
        # Two Stacks
        self.instack = []
        self.outstack = []
        
    def enqueue(self,element):
        self.instack.append(element)
        
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
                
        return self.outstack.pop()
    
    
    
q = Queue2Stacks()

q.enqueue(4)
q.enqueue(44)
q.enqueue(444)
q.enqueue(4444)

q.dequeue()
