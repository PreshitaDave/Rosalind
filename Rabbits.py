# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:42:02 2019

@author: Presh
"""

young=1
mature=0
justmature=0
k = 4
n = 32
for i in range(2,n):
    mature+=justmature 
    justmature=young
    young=mature*k
    total = young+mature+justmature
print(total)