# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:20:31 2021

@author: Toan Thang
"""


    
#%%
import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  # don't remove when you submit for grading
    pass # replace this pass (a do-nothing) statement with your code
    for i in range(10):
        print(random.randint(1,6))
