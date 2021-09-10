#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:08:29 2021

@author: pantea
"""

fileName = input("Enter file name : ")
try:
    fhand = open(fileName)
except:
    print("Error")
    
NumOfHours = dict()
   
for line in fhand:
    if "From " in line :
        words = line.split()
        time = words[5]
        hour = time[:2]
        NumOfHours[hour] =  NumOfHours.get(hour,0) + 1
        
lists = list()
for h,t in NumOfHours.items():
    lists.append((h,t))
    
lists.sort()

for k,v in lists:
    print(k,v)