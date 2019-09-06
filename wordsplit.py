# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:59:40 2019

@author: tony
"""

def word_split(phrase, list_of_words,output = None):
    if output is None:
        output = []
        
    for word in list_of_words:
        if phrase.startswith(word):
            
            output.append(word)
            return word_split(phrase[len(word):],list_of_words,output)
        
    return output

word_split('fourqueuedequestaque',['four','queue','deque','staque'])