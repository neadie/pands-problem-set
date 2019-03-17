# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:06:07 2019

@author: Sinead Frawley

Question 1
"""


import Enternumber as En

def sumUpTo(number):
    if number > 0:
        total=1
        while(number > 1):
            total=total+number
            number=number-1
        return total

print(sumUpTo(En.enterFloat()))