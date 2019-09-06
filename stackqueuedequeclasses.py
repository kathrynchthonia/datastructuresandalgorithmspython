# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 01:28:55 2019

@author: tony
"""
#Stack
class Stack(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
s = Stack()

s.push(4)
s.push(9)
s.pop()
s.isEmpty()
s.peek()
s.size()

#Queue    
class Queue(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    
q = Queue()

q.enqueue(4)
q.enqueue('four')
q.dequeue()
q.peek()
q.size()
q.isEmpty()
   

# Deque 
class Deque(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def addFront(self,item):
        return self.items.append(item)
    
    def addLast(self, item):
        return self.items.insert(0,item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeLast(self):
        return self.items.pop(0)
    
    def peekFront(self):
        return self.items[-1]
    
    def peekLast(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    
d= Deque()

d.isEmpty()
d.addFront(4)
d.addFront(0)
d.addLast(9999)
d.peekFront()
d.peekLast()
d.size()
d.removeFront()
d.removeLast()

        
    