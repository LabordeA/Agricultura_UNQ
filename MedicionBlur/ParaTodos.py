#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:07:48 2019

@author: braso
"""


import cv2
import numpy as np
import time 
import matplotlib.pyplot as plt 
from glob import glob

#start_time = time.time()
videos=glob("/home/braso/Escritorio/Videos calib 191113/*.MP4")
videos.sort()
LapALL=[]

for vid in videos :
    cap = cv2.VideoCapture(vid)
    tamFrame=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
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
        if tamFrame == counter:
            break
    LapALL.append(Laplacian)
    cap.release()
    cv2.destroyAllWindows()


#end_time= time.time()
#
#print("Elapsed time: %.10f seconds." % (end_time - start_time))
