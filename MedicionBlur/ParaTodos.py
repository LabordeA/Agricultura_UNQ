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
starts=np.load('/home/braso/Agricultura_UNQ/MedicionBlur/starts.npy')
ends=np.load('/home/braso/Agricultura_UNQ/MedicionBlur/ends.npy')


for index,vid in enumerate(videos) :
    print(vid)
    print(index)
    cap = cv2.VideoCapture(vid)
    tamFrame=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if (cap.isOpened()== True): 
        print("Opening video stream or file")
    Laplacian=[]
    cap.set(cv2.CAP_PROP_POS_FRAMES,starts[index]+40)
    cont=starts[index]
    while(cap.isOpened()):
        ret, frame = cap.read()
        cont+=1
        print('\r' , cap.get(cv2.CAP_PROP_POS_FRAMES),end='')
        if (cont == ends[index]):
            break
        if( ret != False):
            lap=cv2.Laplacian(frame,cv2.CV_64F).var()
            Laplacian.append(lap)
        else:
            cap.release()
    LapALL.append(Laplacian)
    print('\n')

np.save('/home/braso/Agricultura_UNQ/MedicionBlur/Laplacian_ALLPITCHDOWN.npy',LapALL)

#end_time= time.time()
#
#print("Elapsed time: %.10f seconds." % (end_time - start_time))
