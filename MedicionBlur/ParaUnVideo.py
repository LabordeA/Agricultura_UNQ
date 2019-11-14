# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:46:10 2019

@author: BraianSoullier
"""

import cv2
import numpy as np
from time import time 
import matplotlib.pyplot as plt 

start_time = time()

cap = cv2.VideoCapture("/home/braso/Escritorio/Videos calib 191113/DJI_0080.MP4")
#cap=cv2.VideoCapture(0)
# Check if camera opened successfully
if (cap.isOpened()== True): 
  print("Opening video stream or file")

counter=0
Laplacian=[]
while(cap.isOpened()):
  ret, frame = cap.read()
  lap=cv2.Laplacian(frame,cv2.CV_64F).var()
  Laplacian.append(lap)
#  counter+=1
#  img=cv2.resize(frame,(1240,640))
##  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#  cv2.imshow('frame',img)   
  print("contador",counter)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
elapsed_time = time() - start_time
print("Elapsed time: %.10f seconds." % elapsed_time)

plt.figure()
plt.plt(Laplacian)