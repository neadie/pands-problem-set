# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:47:01 2019

@author: Sinead Frawley
Question 4
"""

'''https://pynative.com/python-check-user-input-is-number-or-string/ '''

numberImput = input("Please enter a positive integer:")
try:
    integerINput= int(numberImput)
    if integerINput > 0:
        while integerINput > 1:
            if integerINput % 2 == 0:
                integerINput=integerINput/2
            else:
                integerINput=integerINput*3 + 1
            print(integerINput)
except ValueError:
    print("That's not an int!")
    print("No.. input string is not an Integer. It's a string")
    
        
        
    

