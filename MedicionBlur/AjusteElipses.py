#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:11:05 2019

@author: braso's mother
"""

# %% Este es el coodigo generico que venimos haciendo hace mil años, binarizo 
# detecto contornos, filtro por area y guardo el descriptor de area del bounding
# rect. EN VELOCIDADES BAJAS VA COMO TROMPADAS PARA CUALQUIER SHUTTER Y ALTURA
# (llamo velocidades bajas a las de 1 m/s), y capaz ahi ya podemos tener una idea del blureo
# Para las velocidades altas se complica por que parece una linea de cultivo el 
# blureo del punto sobre el patron.(queda una franja negra, se unen los puntos )
# (una pija diria ULI), pero bueno lo mejore un poco con el clahe en la seccion 3
# capaz que anda para generico con el CLAHE para velocidades bajas tambien pero no probe
# por que me dio paja.

import cv2
import numpy as np 
import matplotlib.pyplot as plt
import glob
import os 

# path=''
# folder='4m_4ms_120/'
# files=glob.glob(path+folder+'*.png')
# files.sort()

path=''
#
#folders=[ '4m_1ms_60/','4m_1ms_120/','4m_1ms_240/',
#		  '4m_4ms_60/','4m_4ms_120/','4m_4ms_240/',
#		  '4m_5ms_60/','4m_5ms_120/','4m_5ms_240/']

#
#folders=[ '6m_1ms_60/','6m_1ms_120/','6m_1ms_240/',
#		  '6m_4ms_60/','6m_4ms_120/','6m_4ms_240/',
#		  '6m_5ms_60/','6m_5ms_120/','6m_5ms_240/']
#

folders=[ '8m_1ms_60/','8m_1ms_120/','8m_1ms_240/',
		  '8m_4ms_60/','8m_4ms_120/','8m_4ms_240/',
		  '8m_5ms_60/','8m_5ms_120/','8m_5ms_240/']



def createFoler(name):
	try:
		os.listdir(name)
		print('la carpeta {:s} existe'.format(name))
	except:
		os.mkdir(name)
		print('la carpeta {:s} creada'.format(name))



def AdjustEllipses(path,folder):
	fileList=glob.glob(path+folder+'*.png')
	fileList.sort()
	outputDir=path+folder.replace('/','_')+'contoursRect'
	createFoler(outputDir)
	clahe = cv2.createCLAHE(clipLimit=3,tileGridSize=(5,5))
	if len(fileList)==0:
		Warning('No Hay archivos revisar nombre de\
				   carpeta: {:s} \r\n Pasando....'.format(folder))
		return None
		
	foundEllipses = False
	areas 	= []
	recs 	= []
	elli 	= []
	for file in fileList :
		img 	= cv2.imread(file)
		gray 	= cv2.cvtColor (img , 		 cv2.COLOR_BGR2GRAY)
		gray=clahe.apply(gray)
		_,imgB 	= cv2.threshold(gray,0, 255, cv2.THRESH_OTSU)
		_,contours,_ = cv2.findContours(imgB,cv2.RETR_TREE,
										cv2.CHAIN_APPROX_NONE)
		
		cv2.imshow('fr',np.hstack([gray,imgB]))
		cv2.waitKey(30)
		
		for cn in contours:
			x,y,w,h 		= cv2.boundingRect(cn)
			rectangulo 	= 255-gray[y:y+h,x:x+w]
			area 		= cv2.contourArea(cn)
			if area<1000 and len(cn)>5:
				elips 	= cv2.fitEllipse(cn)
				recs. append(rectangulo)
				elli. append(elips)
				areas.append(area)
				foundEllipses=True

	data = {'rectangulos':recs,'elipses':elli,'areas':areas}
	np.save(outputDir+'elipsesAjustadas',data)
	if foundEllipses:
		ejes = np.array([[q[1][0],q[1][1]] for q in elli]).T
		plt.scatter(ejes[0],ejes[1],alpha=.3,label = folder)
		#plt.plot(ejes[0]/ejes[1],label = folder)
	else:
		print('no se encontraron elipses en {:s}'.format(folder))

plt.figure()
[AdjustEllipses(path,folder) for folder in folders]
plt.plot([0,25], [0, 25],'b')
plt.legend()
plt.title('Ejes de las elipses ')
plt.ylabel('Eje Mayor [pix]')
plt.xlabel('Eje Menor [pix]')
plt.xlim((-1,26))
plt.ylim((-1,70))

