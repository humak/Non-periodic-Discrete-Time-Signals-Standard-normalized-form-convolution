'''                 functionA.py
Huma Kalayci

'''
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xLowerB = int(sys.argv[1])
xUpperB = int(sys.argv[2])
yLowerB = int(sys.argv[3])
yUpperB = int(sys.argv[4])

lengthX = xUpperB - xLowerB + 1 #1-2
lengthY = yUpperB - yLowerB + 1 #3-4

arrXx = []
arrXy = []

arrYx = []
arrYy = []

for i in range (0,lengthX):
    arrXy.append(int(sys.argv[5+i]))
    arrXx.append(xLowerB + i)
    print('X[',arrXx[i],'] = ',arrXy[i])
for i in range (0,lengthY):
    arrYy.append(int(sys.argv[5+lengthX+i]))
    arrYx.append(yLowerB + i)
    print('X[',arrYx[i],'] = ',arrYy[i])

plt.scatter(arrXx, arrXy, label = 'X', color = '#7adf90')
plt.scatter(arrYx, arrYy, label = 'Y', color = '#f09ded')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Visualization of two non-periodic discrete time signal, X and Y')
plt.legend()
plt.show()
