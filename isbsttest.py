# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:18:22 2019

@author: tony
"""

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        

inf = float('infinity')
negInf = float('-infinity')

def isBST(tree,minVal = neginf,maxVal = inf):
    if tree is None:
        return True
    
    if not minVal <= tree.val <= maxVal:
        return False
    
    return isBST(tree.left,minVal,tree.val) and isBST(tree.right,tree.val,maxVal)

def isBST2(tree,lastNode = [neginf]):
    if tree is None:
        return True
    
    if not isBST2(tree.left,lastNode):
        return False
    
    lastNode[0] = tree.val
    
    return isBST2(tree.right,lastNode)