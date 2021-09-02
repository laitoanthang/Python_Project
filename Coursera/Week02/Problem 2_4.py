# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:20:25 2021

@author: Toan Thang
"""


import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    lis=[]
    for i in range(10):
        lis.append(random.uniform(30,35))
    print(lis)
    