#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:30:49 2019

@author: braso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("/home/braso/Documentos/TAMIU/TAMIUSOULLIER/SCRIPS/gps/fauba.jpg", cv2.IMREAD_GRAYSCALE)

#Coordenadas punto 1 Esquina superior derecha
lat1=-34.592868
lon1=-58.484629
#Coordenadas punto 2
lat2=-34.592861
lon2=-58.484644
#Coordenadas punto 3
lat3=-34.592846
lon3=-58.484794
#Coordenadas punto 4
lat4=-34.592846
lon4=-58.484821
#Coordenadas punto 5
lat5=-34.592847
lon5=-58.484857
#Coordenadas punto 6
lat6=-34.592852
lon6=-58.484912
#Coordenadas punto 7
lat7=-34.592853
lon7=-58.484925
#Coordenadas punto 8
lat8=-34.592863
lon8=-58.485246
#Coordenadas punto 9 Esquina superior izquierda
lat9=-34.592864
lon9=-58.485271
#Coordenadas punto 10
lat10=-34.592867
lon10=-58.485273
#Coordenadas punto 11
lat11=-34.592978
lon11=-58.485292
#Coordenadas punto 12
lat12=-34.593088
lon12=-58.485295
#Coordenadas punto 13 Esquina inferior izquierda
lat13=-34.593119
lon13=-58.485293
#Coordenadas punto 14
lat14=-34.593129
lon14=-58.485282
#Coordenadas punto 19
lat19=-34.593138
lon19=-58.484790
#Coordenadas punto 20
lat20=-34.593137
lon20=-58.484688
#Coordenadas punto 21 Esquina inferior derecha
lat21=-34.593136
lon21=-58.484644
#Coordenadas punto 22
lat22=-34.593125
lon22=-58.484634
#Coordenadas punto 23
lat23=-34.593014
lon23=-58.484627
#Coordenadas punto 24
lat24=-34.592885
lon24=-58.484626

Latitudes=[lat1,lat2,lat3,lat4,lat5,lat6,lat7,lat8,lat9,lat10,lat11,lat12,lat13,
			lat14,lat19,lat20,lat21,lat22,lat23,lat24]

Longitudes=[lon1,lon2,lon3,lon4,lon5,lon6,lon7,lon8,lon9,lon10,lon11,lon12,lon13,
			lon14,lon19,lon20,lon21,lon22,lon23,lon24]

U=np.load("listU.npy")

V=np.load("listV.npy")
# Se resuleve L=A*X, donde L es una matriz de 2*N, A una matriz de transformaciòn
# de 2*N y X es una matriz de N*4. L contiene las coordenadas en el mundo, y X
# las coordenadas digitales 

X=np.zeros([4,len(Latitudes)])
L=np.array([Latitudes,Longitudes])

for i in range (len(Latitudes)-1):
	X[0,i]=U[i]
	X[1,i]=V[i]
	X[2,i]=U[i]*V[i]
	X[3,i]=1

X_pinv=np.linalg.pinv(X)
A=np.dot(L,X_pinv)

np.save('tl_v2.npy',A)

p0_l=[U[12],V[12],Latitudes[12],Longitudes[12]]
#[U[12],V[12],Latitudes[12],Longitudes[12]]

np.save('p0_l_v2.npy',p0_l)





# %% Esto era para seleccionar los puntos de la imagen que corresponden a las
# coordenadas introducidas a mano

#plt.figure()
#plt.imshow(img,'gray')
#
#for i in range (1,20):
#	print('esquina inferior izquierda:\t\n',end=' ')
#	y,x=np.array(np.round(plt.ginput()[0]),dtype=np.int32)
#	U.append(x)
#	V.append(y)