'''                 functionD.py
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
    #print(arrXx[i],',',arrXy[i])
for i in range (0,lengthY):
    arrYy.append(int(sys.argv[5+lengthX+i]))
    arrYx.append(yLowerB + i)
    #print(arrYx[i],',',arrYy[i])


def findMin(arr):
    minVal = None
    for i in arr:
        if not minVal:
            minVal = i
        elif i < minVal:
            minVal = i
    return minVal

def findMax(arr):
    maxVal = None
    for i in arr:
        if not maxVal:
            maxVal = i
        elif i > maxVal:
            maxVal = i
    return maxVal


arrXxNorm = []
arrXyNorm = []

arrYxNorm = []
arrYyNorm = []


minX = findMin(arrXy)
maxX = findMax(arrXy)  
#print('min: ', minX, 'max:', maxX) 
    
minY = findMin(arrYy)
maxY = findMax(arrYy)  
#print('min: ', minY, 'max:', maxY)    

def findNormalValue(val, minV, maxV):
    z = (val - minV)/(maxV-minV)
    return z


for i in range (0,lengthX):
    arrXxNorm.append(arrXx[i])

for i in range (0,lengthY):
    arrYxNorm.append(arrYx[i])


for i in range (0,lengthX):
    z = findNormalValue(arrXy[i], minX, maxX)
    arrXyNorm.append(z)
    #print( 'X[' , arrXxNorm[i],']'  ,'=',arrXyNorm[i])
for i in range (0,lengthY):
    z = findNormalValue(arrYy[i], minY, maxY)
    arrYyNorm.append(z)
    #print( 'Y[' , arrYxNorm[i],']'  ,'=',arrYyNorm[i])


arrXxStaNorm = []
arrXyStaNorm = []

arrYxStaNorm = []
arrYyStaNorm = []

for i in range (0,lengthX):
    arrXxStaNorm.append(arrXx[i])

for i in range (0,lengthY):
    arrYxStaNorm.append(arrYx[i])


for i in range (0,lengthX):
    arrXyStaNorm.append(0)

for i in range (0,lengthY):
    arrYyStaNorm.append(0)



sumOfx = 0
sumOfy = 0
for i in range (0,lengthX):
    sumOfx += arrXyNorm[i]
for i in range (0,lengthY):
    sumOfy += arrYyNorm[i]

sumX = 0
sumY = 0
meanOfX = 0
meanOfY = 0

meanOfX = sumOfx / lengthX
meanOfY = sumOfy / lengthY


for i in arrXyNorm:
    sumX = sumX + (  float(  (float(i) - meanOfX) ) * float(  (float(i) - meanOfX) )  )
for i in arrYyNorm:
    sumY = sumY + (  float(  (float(i) - meanOfY) ) * float(  (float(i) - meanOfY) )  )

derX = sumX / lengthX
derY = sumY / lengthY

derX = np.sqrt(derX)
derY = np.sqrt(derY)


print('Standard normalized form of the signals X and Y :')
for i in range (0,lengthX):
    arrXyStaNorm[i] = (arrXyNorm[i] - meanOfX) / derX
    print( 'X[' , arrXxStaNorm[i],']'  ,'=',arrXyStaNorm[i])

for i in range (0,lengthY):
    arrYyStaNorm[i] = (arrYyNorm[i] - meanOfY) / derY
    print( 'Y[' , arrYxStaNorm[i],']'  ,'=',arrYyStaNorm[i])

#########
sumLen = lengthX + lengthY -1

conv = [0] * sumLen
print()
print('Convolution of the signals X and Y:')
for i in range (0,lengthX):
    for j in range (0,lengthY):
        conv[i+j] += arrXyStaNorm[i] * arrYyStaNorm[j]
        
for i in range (0, sumLen):
    print(conv[i])
