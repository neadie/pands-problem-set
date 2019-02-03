# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:30:42 2019

@author: Sinead Frawley
Question 2
"""

import datetime
my_date = datetime.datetime.now()
dayOfTheWeek=my_date.strftime("%A")
if(dayOfTheWeek.startswith('T')):
    print("Yes - today begins with a T.")
else:
    print("No - today does not begin with a T.")