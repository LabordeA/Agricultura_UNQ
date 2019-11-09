#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:44:02 2019

@author: nicolascuedo
"""

import numpy as np
import time
import smopy
import cv2
from matplotlib import pyplot as plt
from numpy import array


path="/home/nicolascuedo/Escritorio/TAMIU_Octubre/Otros/Uli_mail/analisisCampo/VideoTestGui/VidCam1_6_5_19222_conts2.avi"


clahe = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(8,8))

def GiCont(img, umbral=100):
	#imSize = img.shape
	hue,sat,val = cv2.cvtColor(img,cv2.COLOR_BGR2HSV).transpose(2,0,1)
	nval = clahe.apply(val)
#	nsat = clahe.apply(sat)
	newImg = cv2.cvtColor(np.array([hue,sat,nval]).transpose(1,2,0),cv2.COLOR_HSV2BGR)
	
	ch_b,ch_g,ch_r = newImg.transpose(2,0,1)
	greenIndex  = (2.0*ch_g-ch_r-ch_b)
	g_I_Umbral  = greenIndex >umbral
	
	mask1 = ch_g > (np.uint16(ch_r)+20)
	mask2 = ch_g > (np.uint16(ch_b)+20)
	mask3 = np.uint8(mask1*mask2)
	
	e=2
	se = np.ones([e,e])
	d=12
	sd = np.ones([d,d])
	g_I_UmbralEroded  = cv2.erode(np.uint8(1*g_I_Umbral*mask3),se)
	g_I_UmbralDilated = cv2.dilate(g_I_UmbralEroded,sd)
	g_I_UmbralDilated = cv2.morphologyEx(g_I_UmbralDilated, cv2.MORPH_CLOSE, np.ones([7,7]))

	
	
	im2, contours, hierarchy = cv2.findContours(g_I_UmbralDilated, 
											 cv2.RETR_TREE, 
											 cv2.CHAIN_APPROX_SIMPLE)
	
	return newImg,contours

# %%
	
c1 = cv2.VideoCapture(path)
c1.set(cv2.CAP_PROP_POS_FRAMES,10)
l1 = c1.get(cv2.CAP_PROP_FRAME_COUNT)
contourList = []
for i in range(int(l1-50)):
		ret,img = c1.read()
		if ret:
			#imf = GvRBCalc(img)
			newImg,contours = GiCont(img)
			contourList.append(contours)
			imgOut = cv2.drawContours(np.copy(newImg),contours,-1,(0,0,255),thickness=3)
			cv2.imshow('fr',imgOut)
			if cv2.waitKey(0)==ord('q'):
				break
			if not i%150:
				print('\r',i,' de ', l1-60,end="")
		else:
			break

#
#for():
#	newImg,contours = GiCont(img)
#			contourList.append(contours)
#			imgOut = cv2.drawContours(np.copy(newImg),contours,-1,(0,0,255),thickness=3)
#			cv2.imshow('fr',imgOut)
#			if cv2.waitKey(0)==ord('q'):
#				break
#	