# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:54:08 2019

@author: Sinead Frawley

Question 8
"""

import datetime
my_date = datetime.datetime.now()
dayOfTheWeek=my_date.strftime("%A")
monthOftheYear=my_date.strftime("%B")
dateOfMonth=my_date.strftime("%d")
year=my_date.strftime("%Y")
currentTime=my_date.strftime("%I:%M:%S %p")
print(dayOfTheWeek + ', '+ monthOftheYear + ' '+dateOfMonth+'th '  + year + ' at ' + currentTime)
'''Monday, January 10th 2019 at 1:15pm'''