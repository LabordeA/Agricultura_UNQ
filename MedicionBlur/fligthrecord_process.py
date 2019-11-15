#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:02:09 2019

@author: braso
"""

import pandas as pd 
import matplotlib.pyplot as plt
import cv2
import numpy as np
from time import time
import glob

a1=time()
files=glob.glob("/home/braso/Escritorio/Videos calib 191113/FligthRecord/*.csv")
ALL_Vel=[]
ALL_Height=[]

for file in files:
    dt_frame= pd.read_csv(file,encoding = "ISO-8859-1")
    list_Vel=[]
    list_Height=[]
    
    for i in range(len(dt_frame)):
        if(dt_frame["CUSTOM.isVideo"][i]=="Recording" and dt_frame["CUSTOM.hSpeed [m/s]"][i]!=0):
            list_Vel.append(dt_frame["CUSTOM.hSpeed [m/s]"][i])
            list_Height.append(dt_frame["OSD.height [m]"][i])
        if(dt_frame["CUSTOM.isVideo"][i]=="Stop" and (len(list_Vel)!=0)):
            ALL_Vel.append(list_Vel)
            ALL_Height.append(list_Height)
            list_Vel=[]
            list_Height=[]
            print(i,"de",len(dt_frame))

a2=time()

print ("Esto tardo",np.round(a2-a1,2),"segundos")

def moda(datos):
    repeticiones = 0

    for i in datos:
        n = datos.count(i)
        if n > repeticiones:
            repeticiones = n

    moda = [] #Arreglo donde se guardara el o los valores de mayor frecuencia 

    for i in datos:
        n = datos.count(i) # Devuelve el número de veces que x aparece enla lista.
        if n == repeticiones and i not in moda:
            moda.append(i)

    if len(moda) != len(datos):
        print ('Moda: ', moda)
    else:
        print ('No hay moda')
    return moda

Velocidades=[]
Height=[]
for j in range (len(ALL_Vel)) :
    v=moda(ALL_Vel[j])
    h=moda(ALL_Height[j])
    Velocidades.append(max(v))
    Height.append(max(h))


np.save("list_Vel.npy",Velocidades)
np.save("list_Height.npy",Height)
