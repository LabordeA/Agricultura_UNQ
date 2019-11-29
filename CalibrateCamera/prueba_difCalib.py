#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:00:00 2019

@author: braso
"""

import cv2
import glob
import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt

#ruta = r"C:/Users/BraianSoullier/Desktop/TAMIUSOULLIER/FAUBA_190904/Code/imgOrig.png"
#path="/home/nicolascuedo/Escritorio/TAMIU_Octubre/SCRIPS/CorrecDeDist/"
photo = "/home/braso/Agricultura_UNQ/CalibrateCamera/ParaCalibrar_4k_60/vlcsnap-2019-11-26-19h06m49s221.png"
imgOrig = cv2.imread(photo)
pars1 = np.load('/home/braso/Agricultura_UNQ/CalibrateCamera/ParaCalibrar_4k_60/camParameters.npy',allow_pickle=True).item()
pars2=np.load('/home/braso/Agricultura_UNQ/CalibrateCamera/ParaCalibrar_4k_240/camParameters.npy',allow_pickle=True).item()

#%% Corrigo distorción de imagen con parametros de la camara sacados en del script "calibracion.py"
x=np.linspace(-.5,.5,200)


def dist(x, distCoeffs, cameraMatrix):
	r2=x**2
	r4 = r2**2
	r6 = r2*r4
	k1, k2, p1, p2, k3 = distCoeffs.reshape(-1)
	
	x2 = x * (1 + k1 * r2 + k2 * r4 + k3 * r6) + p2 * 3 * r2
	u = cameraMatrix[0, 0] * x2 + cameraMatrix[0, 2]
	return u



u1 =dist(x,pars1['distCoeffs'],pars1['cameraMatrix'])
u2 =dist(x,pars2['distCoeffs'],pars2['cameraMatrix'])

plt.plot(x,u1)
plt.plot(x,u2)


f1= cv2.undistort(imgOrig,pars1['cameraMatrix'],pars1['distCoeffs'])
f2= cv2.undistort(imgOrig,pars2['cameraMatrix'],pars2['distCoeffs'])
plt.figure()
plt.imshow(f1-f2)