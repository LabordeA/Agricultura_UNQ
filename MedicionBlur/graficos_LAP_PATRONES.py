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

# %%  Graficos para el informe del TPF
vels=np.round(vels)
heights_string = heights.astype('U')
for n,i in enumerate(vels):
    if i==3:
        vels[n]=4
vels_string=vels.astype('U')

for d in range(len(data)):
	if (d  !=  9) and (d != 10) and (d !=  11) :
		
		plt.figure('Fligth over' + heights_string[d] +'meters altitud at '+ vels_string[d])
		plt.plot(data[d],linewidth = 3.0,label="Shutter:"+shutter[d])
		plt.xlabel('Frames',fontsize="x-large")
		plt.ylabel('Varianza del Laplaciano',fontsize="x-large")
		plt.legend(loc=1,fontsize="xx-large")
		plt.title('Volando a ' + heights_string[d] +'m a una velocidad de '+ vels_string[d]+' m/s',fontsize="x-large")
		
		plt.figure('Fligth over' + heights_string[d] +'meters altitud at '+ shutter[d])
		plt.plot(data[d],linewidth = 3.0,label="Vel:"+ vels_string[d]+' m/s')
		plt.xlabel('Frames',fontsize="x-large")
		plt.ylabel('Varianza del Laplaciano',fontsize="x-large")
		plt.legend(loc=1,fontsize="xx-large")
		plt.title('Volando a ' + heights_string[d] +'m con un Shutter speed de '+ shutter[d],fontsize="x-large")
		
		plt.figure('Variando el shutter' + shutter[d] +'meters altitud at '+ vels_string[d])
		plt.plot(data[d],linewidth = 3.0,label="Altura:"+ heights_string[d]+' m')
		plt.xlabel('Frames',fontsize="x-large")
		plt.ylabel('Varianza del Laplaciano',fontsize="x-large")
		plt.legend(loc=1,fontsize="xx-large")
		plt.title('Volando con shutter speed de ' + shutter[d] +' a una velocidad de '+ vels_string[d]+' m/s',fontsize="x-large")