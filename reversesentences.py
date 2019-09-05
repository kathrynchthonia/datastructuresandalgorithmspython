# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:19:45 2019

@author: tony
"""

#Sentence Reversal
def rev_words1(s):
    return ' '.join(reversed(s.split()))

def rev_words2(s):
    return ' '.join(s.split()[::-1])
    
def rev_words3(s):
    words = []
    length = len(s)
    spaces = [' ']
    
    i = 0 
    
    while i < length:
        if s[i] not in spaces:
            
            word_start = i
            while i< length and s[i] not in spaces:
                
                i+= 1
                
            words.append(s[word_start:i])
            
        i+= 1
        
    return ' '.join(reversed(words))

rev_words3('Ninjas in the darkness')

rev_words1('Ninjas in the darkness')

rev_words2('Ninjas in the darkness')