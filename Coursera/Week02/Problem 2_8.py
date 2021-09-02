# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:20:49 2021

@author: Toan Thang
"""
#%%

hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]

def max(temp_list):
    max = temp_list[0]
    for i in temp_list:
        if (i>max): max = i
    return max

def min(temp_list):
    min = temp_list[0]
    for i in temp_list:
        if (i<min): min = i
    return min
    
def sum(temp_list):
    sum = 0
    for i in temp_list:
        sum += i;
    return sum


def problem2_8(temp_list):
    print("Average:",sum(temp_list)/len(temp_list))
    print("High:", max(temp_list))
    print("Low", min(temp_list))