#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:47:53 2019

@author: braso
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np

img=cv2.imread('/home/braso/Agricultura_UNQ/MedicionBlur/4m_1ms_240/103.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img,"gray")
print('borde 1:\t',end=' ')
y1,x1=np.array(np.round(plt.ginput()[0]),dtype=np.int32)
print('borde 2:\t\n',end=' ')
y2,x2=np.array(np.round(plt.ginput()[0]),dtype=np.int32)

# En pixel
diametro=y2-y1

print('Diametro de un punto del patron en pixel',diametro)


# %% 
# Para calibracion de shutter 240

vels=[1,4,5] # [m/s]
deltaT=[1/60,1/120,1/240] #[s]
fx=4545.52 # En [Pixels]
fy=4542.18 # En [pixels]
hx=5.6819 # en [m]
hy=5.6772 # en [m]

for i in deltaT:
	for j in vels:
		ejeX=i*j
		deltaP_x=(fx/hx)*(ejeX)
		deltaP_y=(fy/hy)*(ejeX)
		plt.figure('Dist_X');plt.plot(ejeX,deltaP_x,'+');plt.title('DELTA_X vs VEL*DELTA_T');plt.xlabel('v*delta_T');plt.ylabel('DeltaPix_x')
		plt.figure('Dist_Y');plt.plot(ejeX,deltaP_y,'o');plt.title('DELTA_Y vs VEL*DELTA_T');plt.xlabel('v*delta_T');plt.ylabel('DeltaPix_y')
		

for k in vels:
	dist_X_60=(fx/hx)*deltaT[0]*k
	dist_X_120=(fx/hx)*deltaT[1]*k
	dist_X_240=(fx/hx)*deltaT[2]*k
	dist_Y_60=(fy/hy)*deltaT[0]*k
	dist_Y_120=(fy/hy)*deltaT[1]*k
	dist_Y_240=(fy/hy)*deltaT[2]*k
	plt.figure('Dist_X_60');plt.plot(k,dist_X_60,'+');plt.title('DELTA_X vs VEL');plt.xlabel('v');plt.ylabel('DeltaPix_x')
	plt.figure('Dist_X_120');plt.plot(k,dist_X_120,'+');plt.title('DELTA_Y vs VEL');plt.xlabel('v');plt.ylabel('DeltaPix_x')
	plt.figure('Dist_X_240');plt.plot(k,dist_X_240,'+');plt.title('DELTA_X vs VEL');plt.xlabel('v');plt.ylabel('DeltaPix_x')
	plt.figure('Dist_Y_60');plt.plot(k,dist_Y_60,'o');plt.title('DELTA_Y vs VEL');plt.xlabel('v');plt.ylabel('DeltaPix_Y')
	plt.figure('Dist_Y_120');plt.plot(k,dist_Y_120,'o');plt.title('DELTA_Y vs VEL');plt.xlabel('v');plt.ylabel('DeltaPix_Y')
	plt.figure('Dist_Y_240');plt.plot(k,dist_Y_240,'o');plt.title('DELTA_Y vs VEL');plt.xlabel('v');plt.ylabel('DeltaPix_Y')
