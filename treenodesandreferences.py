# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:50:10 2019

@author: tony
"""

#Representing a tree - Nodes and References
class BinaryTree():
    
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
                
    def getRightChild(self):
        return self.rightChild
        
    def getLeftChild(self):
        return self.leftChild
        
    def setRootVal(self,obj):
        self.key = obj
            
    def getRootVal(self):
        return self.key
    # internal order functions
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    
    def inorder(self):
        if self.leftChild:
                self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)
        pass
        
#External order functions Best practice
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
def postorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRootVal())
        
def inorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        print(tree.getRootVal()) 
        preorder(tree.getRightChild())
              
        
r = BinaryTree('a')
            
r.getRootVal()
r.getLeftChild()
r.insertLeft('of the')
r.insertRight('crescent moon')
r.setRootVal('ninja')
r.getRightChild()

r.getLeftChild().insertRight('NLP')


r.inorder()
r.postorder()
r.preorder()