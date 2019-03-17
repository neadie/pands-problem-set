# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:46:18 2019

@author: Sinead Frawley
Question 7
"""

''' https://stackoverflow.com/questions/47362844/using-an-input-variable-in-multiple-functions-in-python '''




import Enternumber as En

def getSquareRoot(number):
    if number > 0:
        square_number = number**(1.0/2)
        print(square_number)
        
getSquareRoot(En.enterFloat())
        
        