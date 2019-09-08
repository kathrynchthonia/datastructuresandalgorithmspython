# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 05:21:04 2019

@author: tony
"""

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        
        
def trimbst(tree,minVal,maxVal):
    
    if not tree:
        return
    
    tree.left = trimbst(tree.left,minVal,maxVal)
    tree.right = trimbst(tree.right,minVal,maxVal)
    
    if minVal <= tree.val <= maxVal:
        return tree
    if tree.val < minVal:
        return tree.right
    
    if tree.val > maxVal:
        return tree.left