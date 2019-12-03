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







fIdx = ([0,1],[0,1])
cIdx= ([0,1],[-1,-1])


header = """\r\n
	__________________________________________________________________________
	 Carpeta: \t  {:s}
	 __________________________________________________________________________
			Cantidad de archivos de calibración: \t {:d} \n
"""

tabla="""
   _____________________________________
  |\t    {:s}  \t|
  |_____________________________________|
  |___|______media______|_______std_____|
  | X |   {:.3f}\t|   {:.3f}\t|
  | Y |   {:.3f}\t|   {:.3f}\t|
  |_____________________________________|
"""

lMaker =lambda n,f :[n,f.mean(0)[0],f.std(0)[0], f.mean(0)[1],f.std(0)[1]] if\
				 isinstance(n,str) else Exception


folders = glob.glob('*/')
def getpars(folder = 'ParaCalibrar_4k_60/'):
	files=glob.glob(folder +'CP_dist*.npy')
	f = np.zeros([len(files),2])
	c = np.zeros([len(files),2])
	for i,file in enumerate(files):
		cameraMatrix =np.load(file,allow_pickle=True).item()['cameraMatrix']
		f[i]  = cameraMatrix[fIdx]
		c[i]  = cameraMatrix[cIdx]
	
	tablas = header.format(folder,len(files)) +'\r\n'+\
		tabla.format(*lMaker('Distancias Focales',f))+'\r\n'+\
		tabla.format(*lMaker('Centros de imagenes',c))
	print(tablas)
	
	with open('parametrosConMedia.txt','a') as file:
		file.write(tablas)


"""Creo Y cierro el archivo, para no agregar otra vez todo"""
with open('parametrosConMedia.txt','w') as file:
	file.write('Tabla generada automáticamente\r\n\r\n')

[getpars(f) for f in folders]