#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:28:07 2019

@author: braso
"""
# %%


import cv2
import glob
import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt

areas=[]
moments=[]
img=cv2.imread('/home/braso/Agricultura_UNQ/MedicionBlur/4m_1ms_240/86.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ja,imgB=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#	cv2.drawContours(imgB,cnt,-1,(127,0,0),2)
for cn in cnt:
	x,y,w,h = cv2.boundingRect(cn)
	rectangulo=imgB[y:y+h,x:x+w]
	area=len(rectangulo)*len(rectangulo[0])
	if(area<220):
		#cv2.rectangle(imgB,(x,y),(x+w,y+h),(127,0,0),2)
		areas.append(area)
		mm=cv2.moments(255-rectangulo)
		moments.append(mm)
#	cv2.imwrite('{:s}/{:s}'.format(outputDir,file.split(path+folder)[1]),imgB)
