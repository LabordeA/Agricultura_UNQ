#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:30:13 2019

@author: braso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

data= np.load("/home/braso/Agricultura_UNQ/MedicionBlur/blur_allvideos.npy",allow_pickle=True)
vels=np.load("list_Vel.npy")
heights=np.load("list_Height.npy")
shutter=np.load("shutters.npy")
coun4=0
coun6=0
coun8=0








for d in range(len(data)):
    if(3.5<=heights[d]<=4.5):
        coun4+=1
        if(vels[d]<1):
            plt.figure("Fligth over 4 meters altitud at 1 m/s")
            plt.plot(data[d],label="Shutter="+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around all video ")
        if(2<vels[d]<4):
            plt.figure("Fligth over 4 meters altitud at 4 m/s")
            plt.plot(data[d],label="Shutter="+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around all video ")
        if(4.5<vels[d]<6):
            plt.figure("Fligth over 4 meters altitud at 6 m/s")
            plt.plot(data[d],label="Shutter="+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around all video ")

    if(5.5<=heights[d]<=6.5):
        coun6+=1
        if(vels[d]<1):
            plt.figure("Fligth over 6 meters altitud at 1 m/s")
            plt.plot(data[d],label="Shutter="+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around all video ")
        if(2<vels[d]<4):
            plt.figure("Fligth over 6 meters altitud at 4 m/s")
            plt.plot(data[d],label="Shutter="+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around all video ")
        if(4.5<vels[d]<6):
            plt.figure("Fligth over 6 meters altitud at 6 m/s")
            plt.plot(data[d],label="Shutter="+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around all video ")
    if(7.5<=heights[d]<=8.5):
        coun8+=1
        if(vels[d]<1):
            plt.figure("Fligth over 8 meters altitud at 1 m/s")
            plt.plot(data[d],label="Shutter="+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around all video ")
        if(2<vels[d]<4):
            plt.figure("Fligth over 8 meters altitud at 4 m/s")
            plt.plot(data[d],label="Shutter="+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around all video ")
        if(4.5<vels[d]<6):
            plt.figure("Fligth over 8 meters altitud at 6 m/s")
            plt.plot(data[d],label="Shutter="+shutter[d])
            plt.legend()
            plt.title("laplacian matrix around all video ")
            
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

