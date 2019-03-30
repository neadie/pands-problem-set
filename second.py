# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:41:56 2019  reference - https://www.afterhoursprogramming.com/tutorial/python/reading-files/

@author: SineadF
"""
'''https://www.geeksforgeeks.org/reading-writing-text-files-python/ '''
'''Question 9 


''' 
''' Change working directory in python '''
  

''' To call this file is second.py " what ever file name you what to call if in same direcory just file name if in another 
 directory path of file is required too
 
 '''
import sys

def everySecondLine(fileName):
    f = open(fileName, "r") #opens file with name of "test.txt"
    '''The r can be ignored if the file is in same directory and address is not being placed. '''
    myList = []
    for line in f:
        myList.append(line)
    f.close()
    everySecondLine = myList[::2]
    print(everySecondLine)    

args = sys.argv[1:]
print(args[0])
print(everySecondLine(args[0]))