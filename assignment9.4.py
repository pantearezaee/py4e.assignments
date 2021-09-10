#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:59:40 2021

@author: pantea
"""

name = input("Enter file name : ")
fhand = open(name)
senders = dict()

for lines in fhand:
    lines.rstrip()
    if "From " in lines:
        words = lines.split()
        senders[words[1]] =  senders.get(words[1],0) + 1
        
bigsender = None
numbersent = None

for sender,number in senders.items():
    if bigsender is None or numbersent < number:
        bigsender = sender
        numbersent = number
        
print(bigsender,numbersent)