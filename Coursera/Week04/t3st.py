# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:08:17 2021

@author: Toan Thang
"""


def fizzBuzz(n):
    for i in n:
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0 and i%5!=0:
            print("Fizz")
        elif i%5==0 and i%3!=0:
            print("Buzz")
        else:
            print(i)
    return


if __name__ == '__main__':
    #n = int(input().strip())
    n = int(input("Input n ="))
    fizzBuzz(n)
