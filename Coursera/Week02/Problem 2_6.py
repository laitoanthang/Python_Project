# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:20:37 2021

@author: Toan Thang
"""


#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    pass # replace this pass (a do-nothing) statement with your code
    for i in range(100):
        print(random.randint(1,6)+random.randint(1,6))
