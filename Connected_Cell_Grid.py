# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 01:40:56 2015

@author: Enes Kemal Ergin

Connected Cell in a Grid
"""
"""
m = int(raw_input())
n = int(raw_input())
"""

matrix = [[1,0,0],[0,1,0],[0,0,1]]

count = 0
for i in matrix:
    for j in i:
        if j == 1:
            count += 1
        if i[j+1] and (matrix[i+1][j] or matrix[i+1][j+1]) != 1:
            count  = 0
        
            
print count        