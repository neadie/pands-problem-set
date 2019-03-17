# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:17:11 2019

@author: SineadF
"""
'''Question 10'''
'''https://stackoverflow.com/questions/36347725/how-can-i-square-every-element-in-an-n-by-n-numpy-array '''
''' https://stackoverflow.com/questions/31726643/how-do-i-get-multiple-subplots-in-matplotlib '''
''' https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html ''''
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0., 4., .2)
# red dashes, blue squares and green triangles
lines = plt.plot(t, t, 'r--', t, t**2, 'b--', t, 2**t, 'g--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('plot of the functions x, x2 and 2x in the range [0, 4].')
plt.legend(lines[:3], ['x', 'x2','2x'])
plt.show()