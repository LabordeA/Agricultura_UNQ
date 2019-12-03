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

path=''
folder='4m_4ms_120/'
files=glob.glob(path+folder+'*.png')
files.sort()


def createFoler(name):
	try:
		os.listdir(name)
		print('la carpeta {:s} existe'.format(name))
	except:
		os.mkdir(name)
		print('la carpeta {:s} creada'.format(name))


images=[]
areas=[]
outputDir=path+folder.replace('/','_')+'contoursRect'
createFoler(outputDir)
for file in files :
	img=cv2.imread(file)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ja,imgB=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
	imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#	cv2.drawContours(imgB,cnt,-1,(127,0,0),2)
	r = []
	for cn in cnt:
		x,y,w,h = cv2.boundingRect(cn)
		rectangulo=imgB[y:y+h,x:x+w]
		r.append(rectangulo)
		area=len(rectangulo)*len(rectangulo[0])
		if(area<220):
			#cv2.rectangle(imgB,(x,y),(x+w,y+h),(127,0,0),2)
			areas.append(area)
	images.append(imgB)
#	cv2.imwrite('{:s}/{:s}'.format(outputDir,file.split(path+folder)[1]),imgB)
	print(file)

np.save(outputDir+'/areas.npy',areas)



# %% PRUEBA DE CIRUCLOS CON HUOGH pero no me gusta como da,
 	## seguramente soy yo el burro que no sabe pasar bien los parametos
 	## pero bueno algo da pero esta como el ogt

import cv2
import numpy as np 
import matplotlib.pyplot as plt
import glob

path=''
folder='4m_1ms_240/'
files=glob.glob(path+folder+'*.png')
files.sort()

images=[]
areas=[]
for file in files :

#%%
img=cv2.imread(file)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray=255-gray
# Blur the image to reduce noise
#	img_blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,10,
						param1=30,param2=10,minRadius=1,maxRadius=10)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
	# draw the outer circle
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	# draw the center of the circle
	#cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
plt.imshow(img)
#%%
#	images.append(img)
#	print(file)
	



# # %% Lo mismo que la primera seccion pero le agrego el clahe para equalizar las velocidades mas rapidas
#  	## ya que es una mierda el histograma de los patrones 
# import cv2
# import numpy as np 
# import matplotlib.pyplot as plt
# import glob
# import os 

# path=''
# folder='8m_5ms_240/'
# files=glob.glob(path+folder+'*.png')
# files.sort()

# images=[]
# areas=[]
# outputDir=path+folder.replace('/','_')+'contoursRect'
# createFoler(outputDir)
# for file in files:
#  	img=cv2.imread(file)
#  	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#  	clahe = cv2.createCLAHE(clipLimit=3)
#  	gray=clahe.apply(gray)
#  	ja,imgB=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
#  	imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# #	cv2.drawContours(imgB,cnt,-1,(127,0,0),2)
#  	for cn in cnt:
# 		x,y,w,h = cv2.boundingRect(cn)
# 		rectangulo=imgB[y:y+h,x:x+w]
# 		area=len(rectangulo)*len(rectangulo[0])
# 		if(area<400):
#  			cv2.rectangle(imgB,(x,y),(x+w,y+h),(127,0,0),2)
#  			areas.append(area)
#  	images.append(imgB)
#  	cv2.imwrite('{:s}/{:s}'.format(outputDir,file.split(path+folder)[1]),imgB)
#  	print(file)

# #np.save(outputDir+'/areas.npy',areas)
