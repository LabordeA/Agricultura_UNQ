#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:50:02 2020

@author: braso
"""

import numpy           as np
import matplotlib.pyplot as plt
import cv2
from glob import glob


#folder = "/home/braso/Agricultura_UNQ/CodigosStiching/Frames/*.jpg"
folder='/home/braso/Agricultura_UNQ/gps/Para SURF/*.PNG'
files =glob(folder)
files.sort()

img=list()

for file in files:
    print()
    img.append(cv2.imread(file, cv2.IMREAD_GRAYSCALE))

img[0]=img[0][210:,0:1346]
img[1]=img[1][:,0:1346]

pts_src=[]
pts_dst=[]

# Selecciona 4 puntos iguales en cada foto, elegis uno en una y el mismo en la otra. 
# Asi hasta completar 4 veces(Trato de que sea las 4 esquinas de una parcela)
for i in range(1,5):
	print(i)
	plt.figure('Seleccionar puntos imagen 1')
	plt.imshow(img[0],'gray')
	print('ELegir un punto de interés:\t\n',end=' ')
	cx1,cy1=np.array(np.round(plt.ginput()[0]),dtype=np.int32)
	print('Punto en x {:.4f}\n punto en y {:.4f} \n'.format(cx1,cy1))
	pts_src.append([cx1,cy1])
	plt.figure('Seleccionar puntos imagen 2')
	plt.imshow(img[1],'gray')
	print('ELegir un punto de interés:\t\n',end=' ')
	cx2,cy2=np.array(np.round(plt.ginput()[0]),dtype=np.int32)
	print('Punto en x {:.4f}\n punto en y {:.4f} \n'.format(cx2,cy2))
	pts_dst.append([cx2,cy2])
	
	
# %% Hago el warpeo
pts_src=np.array(pts_src)
pts_dst=np.array(pts_dst)
h, status = cv2.findHomography(pts_src, pts_dst)
im_out = cv2.warpPerspective(img[0], h, (img[1].shape[0],img[1].shape[0]))
cv2.imshow("Source Image", cv2.pyrDown(img[0]))
cv2.imshow("Destination Image",cv2.pyrDown(img[1]))
cv2.imshow("Warped Source Image",cv2.pyrDown(im_out))

# Me falta ver como pego la imagen warpeada con la de destino, lo de abajo comentado es lo que hicimos con seba para el stitching
#Pero no me da mas la cabeza y tengo noni

aux=np.zeros(im_out.shape, dtype=np.uint8)
aux[:img[0].shape[0], :img[0].shape[1]] =  img[0]
mask = np.any(im_out != 0, axis=1)
Kernel=np.ones([3,3],dtype=np.uint8)
mask=np.uint8(mask)
mask=cv2.erode(mask,Kernel) != 0
aux[mask] = im_out[mask]

plt.figure()
plt.imshow(aux)
plt.title('Stitching')

