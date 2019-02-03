# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:47:01 2019

@author: Sinead Frawley
Question 4
"""

numberImput = input("Please enter a positive integer:")
integerINput= int(numberImput)

while integerINput > 1:
    if integerINput % 2 == 0:
        integerINput=integerINput/2
    else:
        integerINput=integerINput*3 + 1
    print(integerINput)
        
        
    

