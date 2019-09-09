# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 02:19:59 2019

@author: tony
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph,start):
    visited = set()
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
            
    return visited

bfs(graph, 'A') 


#More python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs(graph, nxt,visited)
    return visited

dfs(graph, 'A')

#All possible paths
def dfs_paths(graph,start,goal):
    stack = [(start, [start])]
    while stack:
        (vertex,path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt,path+[nxt]))
                
list(dfs_paths(graph,'A','F'))



