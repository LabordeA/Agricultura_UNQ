#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:30:13 2019

@author: braso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

data1= np.load("/home/braso/Agricultura_UNQ/MedicionBlur/laplacian_80al89.npy",allow_pickle=True)
data2= np.load("/home/braso/Agricultura_UNQ/MedicionBlur/laplacian_90al109.npy",allow_pickle=True)
data=np.concatenate([data1,data2])
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
            plt.figure('Fligth over ' + heights_string[d] +' meters altitud at '+ vels_string[d])
            plt.plot(data[d],label="Shutter:"+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around video with PITCH DOWN")


# %% PLOTEO EL BLUR DEJANDO FIJO LA ALTURA Y LA SHUTTER, Y VARIO LA VELOCIDAD

vels_string=vels.astype('U')
heights_string = heights.astype('U')
for d in range(len(data)):
            plt.figure('Fligth over ' + heights_string[d] +' meters altitud with shutter '+ shutter[d])
            plt.plot(data[d],label="Velocity:"+vels_string[d])
            plt.legend()
            plt.title("laplacian matrix around video with PITCH DOWN")



# %% FALTA MUCHO CARIÑO PERO ME HINCHE LOS HUEVOS 
def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
 
    return sum/len(lista) 

promLap=[]
for dat in range(len(data)):
    prom=promediarLista(data[dat][100:200])
    promLap.append(prom)

plt.figure()
plt.title("Prom Laplacian")
plt.bar(promLap,heights,width=2, align='center')

