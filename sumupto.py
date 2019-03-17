# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:06:07 2019

@author: Sinead Frawley

Question 1
"""

numberImput = input("Please enter a positive integer:")

try:
   integerINput= int(numberImput)
   print("Yes input string is an Integer.")
   print("Input number value is: ", integerINput)
except ValueError:
   print("That's not an int!")
   print("No.. input string is not an Integer. It's a string")


def sumUpTo(number):
    if number > 0:
        total=1
        while(number > 1):
            total=total+number
            number=number-1
        return total

print(sumUpTo(integerINput))