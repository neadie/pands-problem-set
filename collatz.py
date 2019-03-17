# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:47:01 2019

@author: Sinead Frawley
Question 4
"""

'''https://pynative.com/python-check-user-input-is-number-or-string/ '''


import Enternumber as en
def collatz(number):
    if number > 0:
        while number > 1:
            if number % 2 == 0:
                number = number /2
            else:
                number=number*3+1
            print(number)
            

collatz(en.enterint())
      

   

