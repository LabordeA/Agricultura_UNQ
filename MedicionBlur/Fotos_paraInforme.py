#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:35:32 2020

@author: braso
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


for counter,file in enumerate(videos):
	cap = cv2.VideoCapture(file)
	print("Archivo=",file)
	cap.set(cv2.CAP_PROP_POS_FRAMES,250)
	ret, frame = cap.read()
	if(ret!=False):
		img=cv2.resize(frame,(1240,640))
		cv2.imshow('frame',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	else:
		cap.release()

cap.release()