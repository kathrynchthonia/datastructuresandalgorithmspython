# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:34:51 2019

@author: tony
"""

class HashTable(object):
    def __init__(self,size):
        #Set up size and slots of data
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self,key,data):
        #Get the hash value
        hashvalue = self.hashfunction(key,len(self.slots))
        #if Slot is empty
        if self.slots[hashvalue]  == None:
            self.slots[hashvalue] =key
            self.data[hashvalue]=data
            
        else:
            #if key exists replace old value
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
            
            #Get to next slot
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                
                #set new key, if None
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot] = data
                    
                    #else replace old value
                else:
                    self.data[nextslot] = data
            
        
    def hashfunction(self,key,size):
        #remainder method
        return key%size
    
    def rehash(self,oldhash,size):
        #For finding next possible positions
        return (oldhash+1)%size
    
    def get(self,key):
        #Getting items given a key
        
        #Set up variables for our search
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        
        # Until we discern that its not empty or found (and haven't )
        while self.slots[position] != None and not found and not stop:
            
            if self.slots[position] == key:
                found = True
                data= self.data[position]
                
                
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)
        
        
h = HashTable(5)

h[1] = 'one'
h[2] = 'two'
h[3] = 'three'
h[1]

h[1] = 'Ninja'

print(h[4])
            
    
        
        