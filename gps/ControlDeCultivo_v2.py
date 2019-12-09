#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:52:14 2019

@author: braso
"""

import cv2
import glob
import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt
import pandas as pd


from srt_to_csv import srt2csv

# %%
path 	= '/home/ulises/00_Doctorado/MedicionesDrone/'

filExt = 'FAUBA*/'

subtitulos = glob.glob(path+filExt)

for subt in subtitulos:
	srt2csv(subt)


#%%

dt_frames=glob.glob(path+filExt+'/**/'+'DJI_*.csv')
videos=glob.glob(path+filExt+'/**/'+'*.MP4')


# %%
# Print de las coordenadas en el mundo de un punto de interes en la imagen

A=np.load('tl_v2.npy')
img=cv2.imread('/home/ulises/01_TPFs/Cuedo-Soullier/Agricultura_UNQ/CorrecDeDist/Edit_new.jpg', cv2.IMREAD_GRAYSCALE)
plt.figure('Elegir Punto de interes ')
plt.imshow(img,'gray')


print('ELegir un punto de interés:\t\n',end=' ')
cy1,cx1=np.array(np.round(plt.ginput()[0]),dtype=np.int32)

vec=np.array([[cx1],[cy1],[cx1*cy1],[1]])

Coord_Mundo=np.dot(A,vec)
X_mundo=Coord_Mundo[0][0]
Y_mundo=Coord_Mundo[1][0]


print('Latitud y longitud :\t\n',np.round(Coord_Mundo,6))

# %% Referenciar el punto de interes a un Frame del video para buscar la foto ampliada
framesInterest =[]
num = 0

dt_frames 	= np.sort(dt_frames)
videos  	= np.sort(videos)
graficoGPS=False
if graficoGPS:
	for dff in dt_frames:
		df_subt = pd.read_csv(dff)
	
		ll = df_subt[['lat','lon']].valuesdt_frames[5][58:len(dt_frames[5])]
		plt.plot(ll.T[0],ll.T[1],'+')



for dff,vidf in zip(dt_frames,videos):
	
	print(num, ' de ', len(dt_frames))
	print(dt_frames[num][58:len(dt_frames[num])])
	
	df_subt = pd.read_csv(dff)

	puntosLatLon = (df_subt[['lat','lon']])
	puntosLatLon.round(decimals=6)

	Dif = puntosLatLon - (Coord_Mundo[0],Coord_Mundo[1])
	#Dif.round(6)
# minIndex es el frame del video donde se encuentra la imagen a buscar
	tol=1e-5
	index=np.argsort(Dif.abs().values.sum(1))
	latlon=np.sort(Dif.abs().values.sum(1))
	indexInt=index[latlon<tol]
	if(indexInt.size != 0):
		indexInt=np.random.choice(indexInt,5)
	#minIndex = Dif.abs().sum(1).idxmin()
	
	vidcap = cv2.VideoCapture(vidf)
	#Extraer el frame del video
	success,image = vidcap.read()
	f=[]
	for i in indexInt:		
		print('buscando : ',i)
		if (vidcap.set(cv2.CAP_PROP_POS_FRAMES,i)):
			ret, frame = vidcap.read()
			if ret == True:
				f.append(frame)
	vidcap.release()

	framesInterest.append(f)
	num+=1

# %%

for lista in framesInterest:
	for frame in lista:
		print('Procesando')
		if len(frame):
			cv2.imshow('f',cv2.pyrDown(cv2.pyrDown(frame)))
			if cv2.waitKey(0)==ord('q'):
				break
	
cv2.destroyAllWindows()
#FrameInteres=vidcap.set(cv2.CAP_PROP_POS_FRAMES,minIndex)
