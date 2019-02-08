# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:41:56 2019  reference - https://www.afterhoursprogramming.com/tutorial/python/reading-files/

@author: SineadF
"""

'''Question 9 


''' 
''' Change working directory in python '''
import os

os.chdir(r'C:\Users\SineadF\Documents\pands-problem-set')

cwd = os.getcwd()
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files))
print(os.getcwd())
f = open(r"test.txt", "r") #opens file with name of "test.txt"



myList = []
for line in f:
    myList.append(line)
'''Close the file '''
f.close()
''' Get every second line from the list '''
everySecondLine = myList[::2]
print(everySecondLine)