#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys

vstup = ""

offset = 4

vstup_pocet = len(vstup)

vystup = ""
match = 0


for pocatek in range(4):
    match = pocatek 
    for x in range(vstup_pocet):

        if x == match:
            vystup = vystup + vstup[match]
            match = match + offset
    vystup = vystup + "\n"    
print(vystup)






