# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:14:14 2019

@author: Sinead Frawley
Question 5
"""

numberImput = input("Please enter a positive integer:")
integerINput= int(numberImput)

def is_prime_number(x):
   while x >=2:
       for y in range(2,x):
           if not x % y:
               return False
       return True
           
       
    
if is_prime_number(integerINput):
    print("That is a prime.")
else:
    print("That is not a prime.")
    
	        

