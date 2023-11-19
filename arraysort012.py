# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:37:05 2023

@author: nkick
"""

import random

class Solution():
    
    def sort012(self):
        
        self.n =  random.randrange(1 , 6)
        
        self.arr = []
        
        self.count = 0
        
        while self.count <= self.n:
            
            self.arr.append(random.randrange(0 , 3))
            
            self.count += 1
        
        self.arr = sorted(self.arr)
        
        print(self.arr)
    
Solution()



