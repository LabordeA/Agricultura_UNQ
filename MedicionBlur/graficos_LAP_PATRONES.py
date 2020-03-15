#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:47:51 2019

@author: braso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

data= np.load("/home/braso/Agricultura_UNQ/MedicionBlur/laplacian_ONLYPATRONS.npy",allow_pickle=True)
vels=np.load("/home/braso/Agricultura_UNQ/MedicionBlur/list_Vel.npy")
heights=np.round(np.load("/home/braso/Agricultura_UNQ/MedicionBlur/list_Height.npy"))
shutter=np.load("/home/braso/Agricultura_UNQ/MedicionBlur/shutters.npy")

# %% PLOTEO EL BLUR DEJANDO FIJO LA ALTURA Y LA SHUTTER, Y VARIO LA VELOCIDAD
vels=np.round(vels)
heights_string = heights.astype('U')
for n,i in enumerate(vels):
    if i==3:
        vels[n]=4
vels_string=vels.astype('U')

for d in range(len(data)):
	if (d  !=  9) and (d != 10) and (d !=  11) :
		plt.figure('Fligth over' + heights_string[d] +'meters altitud at '+ vels_string[d])
		plt.plot(data[d],label="Shutter:"+shutter[d])
		plt.legend()
		plt.title("laplacian matrix around the patrons")


# %% PLOTEO EL BLUR DEJANDO FIJO LA ALTURA Y LA SHUTTER, Y VARIO LA VELOCIDAD

vels_string=vels.astype('U')
heights_string = heights.astype('U')
for d in range(len(data)):
	if (d  !=  9) and (d != 10) and (d !=  11) :
            plt.figure('Fligth over' + heights_string[d] +'meters altitud with shutter '+ shutter[d])
            plt.plot(data[d],label="Velocity:"+vels_string[d])
            plt.legend()
            plt.title("laplacian matrix around the patrons")

