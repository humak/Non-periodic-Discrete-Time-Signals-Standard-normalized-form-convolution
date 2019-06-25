'''                 functionC.py
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
   # print(arrXx[i],',',arrXy[i])
for i in range (0,lengthY):
    arrYy.append(int(sys.argv[5+lengthX+i]))
    arrYx.append(yLowerB + i)
    #print(arrYx[i],',',arrYy[i])


sumLen = lengthX + lengthY -1

conv = [0] * sumLen


print('Convolution of the signals X and Y:')
for i in range (0,lengthX):
    for j in range (0,lengthY):
        conv[i+j] += arrXy[i] * arrYy[j]
        
for i in range (0, sumLen):
    print(conv[i])











