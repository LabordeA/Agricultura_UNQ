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


files=glob.glob('/home/braso/Agricultura_UNQ/CalibrateCamera/ParaCalibrar_4k_60/*.npy')

f = []
c =[]
for file in files:
	print(file)
	calib=np.load(file,allow_pickle=True).item()
	print(calib['cameraMatrix'])
	f.append(calib['cameraMatrix'][0,0]) 
	f.append(calib['cameraMatrix'][1,1])
	c.append(calib['cameraMatrix'][0,-1])
	c.append(calib['cameraMatrix'][1,-1])

plt.plot(f[::2],'+')
plt.plot(f[1::2],'o')