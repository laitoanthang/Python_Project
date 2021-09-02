# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:20:16 2021

@author: Toan Thang
"""

#%%
newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    for n in ne:
        if (len(n)==1):
            print(n,"has 1 letter")
        print(n,"has", len(n),"letters")
    