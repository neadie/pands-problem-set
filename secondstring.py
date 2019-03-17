# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:14:14 2019

@author: Sinead Frawley
Question 6
"""
def printEverySecondString():
    sentance = input("Please enter a sentence:")
    print(type(sentance))
    sentance = sentance.split(" ")
    print(type(sentance))
    print(sentance[0::2])
    

printEverySecondString()
