# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:14:14 2019

@author: Sinead Frawley
Question 5
"""
import Enternumber as En;

def is_prime_number(x):
   while x >=2:
       for y in range(2,x):
           if not x % y:
               return False
       return True
           
       
 
    
def print_is_or_not_prime():
    if is_prime_number(En.enterint()):
        print("That is a prime.")
    else:
        print("That is not a prime.")
        
''' Call print_is_or_not_prime '''

print_is_or_not_prime()
    
	        

