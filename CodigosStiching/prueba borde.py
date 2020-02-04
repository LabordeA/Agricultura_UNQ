# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 01:48:07 2019

@author: Braso
"""


import numpy             as np
import matplotlib.pyplot as plt
import cv2
from glob import glob

img=cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\stit2.png")
imgB=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
RET,imgB=cv2.threshold(imgB,10,255,0)
imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgB,cnt,-1,(127,0,0))
x,y,ancho,alto=cv2.boundingRect(cnt[0])
_,[altoR,anchoR], _=cv2.minAreaRect(cnt[0])

plt.imshow(imgB)
