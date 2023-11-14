# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:37:05 2023

@author: nkick
"""

import random

n =  random.randrange(1 , 5)
        
arr = []
        
count = 0
        
while count <= n:
            
    arr.append(random.randrange(0 , 3))
            
    count += 1
        
arr = sorted(arr)
        
print(arr)
    


