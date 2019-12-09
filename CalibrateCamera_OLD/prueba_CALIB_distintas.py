#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:09:50 2019

@author: braso
"""

import cv2
import glob
import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt


files=glob.glob('/home/braso/Agricultura_UNQ/CalibrateCamera/calibracion_1_240/*.npy')
files.sort()

fx = []
cx =[]
fy = []
cy =[]
for file in files:
	print(file)
	calib=np.load(file,allow_pickle=True).item()
	print(calib['cameraMatrix'])
	fx.append(calib['cameraMatrix'][0,0]) 
	fy.append(calib['cameraMatrix'][1,1])
	cx.append(calib['cameraMatrix'][0,-1])
	cy.append(calib['cameraMatrix'][1,-1])

fx = np.array(fx)
a = lambda x: 'media: {:.3f}\t desvio:{:.3f}'.format( np.mean(x),np.std(x)) 
print(a(fx))
print(a(fy))
print(a(cx))
print(a(cy))

plt.plot(fx,'+')
plt.plot(fy,'o')