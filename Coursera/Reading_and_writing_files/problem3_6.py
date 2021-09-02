# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:04:26 2021

@author: Toan Thang
"""

import sys

fin = sys.argv[1]
fout = sys.argv[2]

fin = open(fin)
fout = open(fout, 'w')

for line in fin:
    line = line.strip("\n")
    fout.write(str(len(line)) + "\n")

fin.close()
fout.close()