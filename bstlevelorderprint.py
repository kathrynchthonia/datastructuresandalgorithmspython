# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 02:06:11 2019

@author: tony
"""

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


import collections
d = collections.deque([1,2,3])        

def levelOrderPrint(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount = 1
    nextCount = 1
    
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        
        print (currentNode.val)
        
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
            
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount +=1
        if currentCount ==0:
            #print ('\n') 
            currentCount,nextCount = nextCount,currentCount
            
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
levelOrderPrint(root)        