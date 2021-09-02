# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:01:56 2021

@author: Toan Thang
"""

def problem1_7():
    b1 = float(input("Enter the length of one of the bases: "))
    b2 = float(input("Enter the length of the other base: "))
    h = float(input("Enter the height: "))
    print("The area of a trapezoid with bases", str(b1), "and", str(b2), "and height", str(h), "is", (1/2)*(b1+b2)*h)