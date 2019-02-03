# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:06:07 2019

@author: Sinead Frawley

Question 1
"""

numberImput = input("Please enter a positive integer:")
integerINput= int(numberImput)

def sumUpTo(nunber):
    total=1
    while(nunber > 1):
        total=total+nunber
        nunber=nunber-1
    return total

print(sumUpTo(integerINput))