#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:41:32 2021

@author: pantea
"""

import re 

fhand = open("regex_sum_1316316.txt")

integs = list()
summary = 0

#checking for numbers in lines and inserting them
for line in fhand:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    integs = num + integs
    
#converting list items into integers and calculating the sum
for ints in integs:
    summary += int(ints)
    
print(summary)