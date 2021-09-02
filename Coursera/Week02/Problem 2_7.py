# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:20:43 2021

@author: Toan Thang
"""



#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    pass # replace this pass (a do-nothing) statement with your code
    a = float(input("Enter length of side one: "))
    b = float(input("Enter length of side two: "))
    c = float(input("Enter length of side three: "))
    s = 0.5*(a + b + c)
    area = s*(s-a)*(s-b)*(s-c)
    area = area**.5
    print("Area of a triangle with sides",a,b,c,"is",area)
    