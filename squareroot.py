# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:46:18 2019

@author: Sinead Frawley
Question 7
"""

''' https://stackoverflow.com/questions/47362844/using-an-input-variable-in-multiple-functions-in-python '''





    
    
def enterumber():
    numberImput = input("Please enter a positive number:")
    try:
        integerINput= float(numberImput)
        print("Yes input string is an Integer.")
        print("Input number value is: ", integerINput)
        return integerINput
    except ValueError:
        print("That's not an int!")
        print("No.. input string is not an Integer. It's a string")
   


def getSquareRoot(number):
    if number > 0:
        square_number = number**(1.0/2)
        print(square_number)
        
getSquareRoot(enterumber())
        
        