#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:25:47 2020

@author: braso
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

Y1=[3.57,1.24,0.44,118.32,138.66,70.3,109.58,121.66,31.98,4.73,1.39,0.23,97.69,
	105.32,3.16,82.07,87.74,5.73,8.44,2.73,1.18,41.84,103.04,6.05,18,130.66,10.41]

Y05=[2.66,1.2,0.55,22.66,25.93,3.14,109.59,6.89,5.57,7.44,2.82,40.66,4.89,5.82,
	 5.94,0.93,14.44,35.15,13.58,4.22,1.2,4.05,7.71,9.48,2.1,4.79,2.72]

X=[0.002083333333333,0.001041666666667,0.000520833333333,0.008333333333333,
   0.004166666666667,0.002083333333333,0.010416666666667,0.005208333333333,
   0.002604166666667,0.002777777777778,0.001388888888889,0.000694444444444,
   0.011111111111111,0.005555555555556,0.002777777777778,0.013888888888889,
   0.006944444444444,0.003472222222222,0.004166666666667,0.002083333333333,
   0.001041666666667,0.016666666666667,0.008333333333333,0.004166666666667,
   0.020833333333333,0.010416666666667,0.005208333333333]

f=4545
x = np.arange(0, 0.025, 0.001)
y=x*f
plt.figure()
plt.plot(x,y,2.0,c='r')
plt.xlabel('(v.ⵠt)/h',fontsize="x-large")
plt.ylabel('ⵠX[pix]',fontsize="x-large")
plt.title('Comparación modelo geométrico de blur con el ajuste de elipses',fontsize="x-large")
plt.xlim((0,0.005))
plt.ylim((0,20))

for i in range(len(Y1)):
	print(i)
	if(Y1[i] < 25):
		plt.plot(X[i],Y1[i],'o',c='b')
		plt.plot(X[i],Y05[i],'o',c='b')
#plt.figure()
#plt.plot(x,y,2.0,c='r')
#plt.xlabel('(v.ⵠt)/h',fontsize="x-large")
#plt.ylabel('ⵠX[pix]',fontsize="x-large")
#plt.title('Comparación modelo geométrico de blur con el ajuste de elipses-Patrón 0.5 cm',fontsize="x-large")
#plt.xlim((0,0.005))
#plt.ylim((0,20))
#for i in range(len(Y05)):
#	print(i)
#	if(Y05[i] < 25):
#		plt.plot(X[i],Y05[i],'o',c='b')
