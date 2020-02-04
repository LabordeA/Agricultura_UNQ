# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 09:27:36 2019

@author: Braso
"""

import cv2
from time import time
import pandas as pd
import numpy as np


file="D:/Facultad/TAMIU/Videos para calibración 17-07-2019/DJI_0070.MP4"

csvfile = 'D:/Facultad/TAMIU/Videos para calibración 17-07-2019/LOG/FlightRecord'+\
          ' 07-17-2019/DJIFlightRecord_2019-07-17_[14-43-22]csv-verbose/' +\
          'DJIFlightRecord_2019-07-17_[14-43-22]-TxtLogToCsv.csv'


flightLog = pd.read_csv(csvfile,sep=',',engine='python')
#%%
keys = flightLog.keys()
for key in keys:
    if 'eight' in key:
        print(key)
        #%%
indVid,=np.where(flightLog['CUSTOM.isVideo']=='Recording')
indicesDeInteres = indVid[(1.*indVid>8585 )*( 1*indVid<8800)]
for row in file:
    print(row)
    break

df = pd.read_csv(file, sep=';')


#%%

cap =cv2.VideoCapture(file)
print (cap.isOpened())

timeBetweenFrames = 1
desiredSize = (640,480)

desiredFrameNumber = 0
cap.set(cv2.CAP_PROP_POS_FRAMES,desiredFrameNumber)
nFrames =cap.get(cv2.CAP_PROP_FRAME_COUNT)
Blur=[]
while True:
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow('frameName',cv2.resize(frame,desiredSize) )
    frameNum = cap.get(cv2.CAP_PROP_POS_FRAMES)
    framSeg=cap.get(cv2.CAP_PROP_POS_MSEC)
    key = cv2.waitKey(timeBetweenFrames)
    Blur.append(cv2.Laplacian(frame,cv2.CV_64F))
    if  key==ord('q'):#== 0xFF:
        break
    
cv2.destroyAllWindows()
