# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:32:23 2019

@author: SineadF
"""

def enterint():
    numberImput = input("Please enter a positive number:")
    try:
        integerINput= int(numberImput)
        print("Yes input string is an Integer.")
        print("Input number value is: ", integerINput)
        return integerINput
    except ValueError:
        print("That's not an int!")
        print("No.. input string is not an Integer. It's a string")
        
        

def enterFloat():
    numberImput = input("Please enter a positive number:")
    try:
        integerINput= float(numberImput)
        print("Yes input string is an Integer.")
        print("Input number value is: ", integerINput)
        return integerINput
    except ValueError:
        print("That's not an int!")
        print("No.. input string is not an Integer. It's a string")