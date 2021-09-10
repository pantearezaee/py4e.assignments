#!/usr/bin/env python3
# -*- coding: utf-8 -*-
filename = input("Enter file name : ")
fhand = open(filename)
words = list()
count = 0

for line in fhand:
    if "From" in line:
        words = line.split()
        if words[0] =="From:":
           continue
        print(words[1])
        count +=1
        
print("There were", count, "lines in the file with From as the first word")

 


        