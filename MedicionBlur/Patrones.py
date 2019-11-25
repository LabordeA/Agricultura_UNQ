# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:46:10 2019

@author: BraianSoullier
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt 
from glob import glob
import os
#import pandas as pd 
workingDir = '/home/braso/Agricultura_UNQ/MedicionBlur/'
videos=glob("/home/braso/Escritorio/Videos calib 191113/*.MP4")
videos.sort()
shutter_strings=np.load(workingDir+'shutters.npy')
heights=np.round(np.load(workingDir+'list_Height.npy'))
starts=np.load(workingDir+'starts.npy')
ends=np.load(workingDir+'ends.npy')
vels=np.round(np.load(workingDir+'list_Vel.npy'))


def createFoler(name):
	try:
		os.listdir(name)
		print('la carpeta {:s} existe'.format(name))
	except:
		os.mkdir(name)
		print('la carpeta {:s} creada'.format(name))

def umbralContornos(counter):
	umbral=0
	if(shutter_strings[counter]=="1/60."):
		umbral=200-((heights[counter]-min(heights))*5)
	if(shutter_strings[counter]=="1/120"):
		umbral=160-((heights[counter]-min(heights))*5)
	if(shutter_strings[counter]=="1/240"):
		umbral=120-((heights[counter]-min(heights))*5)
	if(shutter_strings[counter]=="1/160"):
		umbral=140
	return umbral

def umbralArea(counter):
	umbralA=0
	if(heights[counter]==4):
		umbralA=4000
	if(heights[counter]==6):
		umbralA=2000
	if(heights[counter]==8):
		umbralA=1000
	return umbralA

def dibujarRec(contornos,imagen,umbralA):
	for cn in contornos:
		x,y,w,h = cv2.boundingRect(cn)
		rectangulo=imagen[y:y+h,x:x+w]
		area=len(rectangulo)*len(rectangulo[0])
		if(area>=umbralA):
			cv2.rectangle(imagen,(x,y),(x+w,y+h),(127,0,0),2)
	return imagen,x,y,w,h 
# %%   Para ver todo los patrones en la ventana "Final"
LapALL=[]
for counter,file in enumerate(videos):
	cap = cv2.VideoCapture(file)
	print("Archivo=",file)
	umbral=umbralContornos(counter)
	umbralA=umbralArea(counter)
	print("umbral del Contorno",umbral)
	print("umbral del Area",umbralA)
	print("Counter",counter)
	outputDir= workingDir +str(int(heights[counter])).replace('.','')+\
							'm_'+str(int(vels[counter])).replace('.','')+\
							'ms_'+shutter_strings[counter].split('/')[-1].replace('.','')
	createFoler(outputDir)
	cap.set(cv2.CAP_PROP_POS_FRAMES,starts[counter]+40)
	cont=starts[counter]
	Laplacian=[]
	while(cap.isOpened()):
		ret, frame = cap.read()
		cont+=1
		if (cont==ends[counter]):
			break
		if(ret!=False):
#			img=frame
			img=cv2.resize(frame,(1240,640))
			cv2.imshow('frame',img)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			ja,imgB=cv2.threshold(gray,umbral,255,cv2.THRESH_BINARY)
			kernel=np.array(([0,1,0],[1,1,1],[0,1,0]),np.uint8)
#			kernel= np.ones([5,5])
			imgB=cv2.morphologyEx(imgB,cv2.MORPH_OPEN,kernel)
			imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
			cv2.drawContours(imgB,cnt,-1,(127,0,0),5)
			cv2.imshow("Contorno",imgB)
#			rect,x,y,w,h=dibujarRec(cnt,img,umbralA)
			for cn in cnt:
				x,y,w,h = cv2.boundingRect(cn)
				rectangulo=img[y:y+h,x:x+w]
				area=len(rectangulo)*len(rectangulo[0])
				if(area>=umbralA):
					cv2.rectangle(np.copy(img),(x,y),(x+w,y+h),(127,0,0),2)
					lap=cv2.Laplacian(rectangulo,cv2.CV_64F).var()
					Laplacian.append(lap)
					cv2.imshow('Patron',rectangulo)
#					cv2.imwrite('{:s}/{:d}.png'.format(outputDir,cont),rectangulo)
#				else:
#					img2= img
			cv2.imshow('Final',img)
			print('\r' , cap.get(cv2.CAP_PROP_POS_FRAMES),end='')
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			cap.release()
	cap.release()
	cv2.destroyAllWindows()
	LapALL.append(Laplacian)
	print('\n')

#np.save('/home/braso/Agricultura_UNQ/MedicionBlur/laplacian_ONLYPATRONS.npy',LapALL)

# %% Prueba de calcular laplaciano dentro del contorno de mayor jerarquia 
	counter=0
	file=videos[counter]
	cap = cv2.VideoCapture(file)
	print("Archivo=",file)
	if(shutter_strings[counter]=="1/60."):
		umbral=200-((heights[counter]-min(heights))*5)
	if(shutter_strings[counter]=="1/120"):
		umbral=160-((heights[counter]-min(heights))*5)
	if(shutter_strings[counter]=="1/240"):
		umbral=120-((heights[counter]-min(heights))*5)
	if(shutter_strings[counter]=="1/160"):
		umbral=140
	print("umbral",umbral)
	print("Counter",counter)
	cap.set(cv2.CAP_PROP_POS_FRAMES,starts[counter]+200)
	ret, frame = cap.read()
	img=cv2.resize(frame,(1240,640))
#	cv2.imshow('frame',img)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	ja,imgB=cv2.threshold(gray,umbral,255,cv2.THRESH_BINARY)
	kernel=np.array(([0,1,0],[1,1,1],[0,1,0]),np.uint8)
#			kernel= np.ones([5,5])
	imgB=cv2.morphologyEx(imgB,cv2.MORPH_OPEN,kernel)
	imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	cv2.drawContours(imgB,cnt,-1,(127,0,0),5)
#	cv2.imshow("Contorno",imgB)
	plt.figure('Frame')
	plt.imshow(img[:,:,::-1])
	plt.figure('contorno')
	plt.imshow(imgB,'gray')
	
	for cn in cnt:
		x,y,w,h = cv2.boundingRect(cn)
		rectangulo=img[y:y+h,x:x+w]
		area=len(rectangulo)*len(rectangulo[0])
		if(area>=5000):
			cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,0),2)

	# Finally show the image
	cv2.imshow('img',img)


# %%
LapALL=[]
for vid in videos :
	cap = cv2.VideoCapture(vid)
	if (cap.isOpened()== True): 
		print("Opening video stream or file")
	counter=0
	Laplacian=[]
	while(cap.isOpened()):
		ret, frame = cap.read()
		counter+=1
		if( ret == True):
			lap=cv2.Laplacian(frame,cv2.CV_64F).var()
			Laplacian.append(lap)
#  counter+=1
#  img=cv2.resize(frame,(1240,640))
##  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#  cv2.imshow('frame',img)   
		print("contador",counter)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	LapALL.append(Laplacian)
	cap.release()
	cv2.destroyAllWindows()


#end_time= time.time()
#
#print("Elapsed time: %.10f seconds." % (end_time - start_time))


# %% Buscando el patron de puntos para hacer una mascara y calcular el laplaciano solo donde aparece el patron NO SIRVE!!!
file=videos[28]
cap = cv2.VideoCapture(file)
#cap.set(cv2.CAP_PROP_POS_FRAMES,570)
while(cap.isOpened()):
	ret, frame = cap.read()
	img=cv2.resize(frame,(1240,640))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray=cv2.resize(gray,(1240,640))
#	cv2.imshow('frame',img)
#	ja,imgB=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
#	ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
	th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,2001,2)
	th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,2001,2)
	cv2.imshow("C1",th2)
	cv2.imshow("C2",th3)
	if cv2.waitKey(1) & 0xFF == ord('q'):
				break
cap.release()
cv2.destroyAllWindows()




