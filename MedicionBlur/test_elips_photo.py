#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:11:05 2019

@author: braso
"""
import cv2
import numpy as np 
import matplotlib.pyplot as plt
import glob
import os 

path='/home/braso/Agricultura_UNQ/MedicionBlur/'
folder='8m_5ms_240/'
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
	for cn in cnt:
		x,y,w,h = cv2.boundingRect(cn)
		rectangulo=imgB[y:y+h,x:x+w]
		area=len(rectangulo)*len(rectangulo[0])
		if(area<220):
			cv2.rectangle(imgB,(x,y),(x+w,y+h),(127,0,0),2)
			areas.append(area)
	images.append(imgB)
	cv2.imwrite('{:s}/{:s}'.format(outputDir,file.split(path+folder)[1]),imgB)
	print(file)

np.save(outputDir+'/areas.npy',areas)


# %%
import cv2
import numpy as np 
import matplotlib.pyplot as plt
import glob

path='/home/braso/Agricultura_UNQ/MedicionBlur'
folder='/4m_1ms_240/'
files=glob.glob(path+folder+'*.png')
files.sort()

images=[]
areas=[]
for file in files :
	img=cv2.imread(file)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ja,imgB=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
	imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#	cv2.drawContours(imgB,cnt,-1,(127,0,0),2)
	for cn in cnt:
		x,y,w,h = cv2.boundingRect(cn)
		rectangulo=imgB[y:y+h,x:x+w]
		area=len(rectangulo)*len(rectangulo[0])
		if(area<200):
			cv2.rectangle(imgB,(x,y),(x+w,y+h),(127,0,0),2)
			areas.append(area)

#	plt.figure(file)
#	plt.imshow(imgB,'gray')
	images.append(imgB)
	print(file)

# %% PRUEBA DE CIRUCLOS CON HUOGH

import cv2
import numpy as np 
import matplotlib.pyplot as plt
import glob

path='/home/braso/Agricultura_UNQ/MedicionBlur'
folder='/4m_1ms_60/'
files=glob.glob(path+folder+'*.png')
files.sort()

images=[]
areas=[]
for file in files :
	img=cv2.imread(file)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Blur the image to reduce noise
	img_blur = cv2.medianBlur(gray, 5)
	circles = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,20,
							param1=15,param2=30,minRadius=0,maxRadius=0)

	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
		# draw the outer circle
		cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
		# draw the center of the circle
		cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
	images.append(img)
	print(file)



