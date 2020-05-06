#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:30:00 2019

@author: nicolascuedo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

import sys
sys.path.append('/home/braso/Agricultura_UNQ/')
import imgTools


path=""
baseDir = '/home/braso/Agricultura_UNQ/gps/' 
lejosDir  = baseDir+'Edit_new.jpg'
al = baseDir + 'stitchAlineado.png'


#img1 = cv2.imread(path+file2,cv2.IMREAD_GRAYSCALE)
img=cv2.imread(lejosDir)


plt.figure()
plt.imshow(img)
s,e = np.int0(plt.ginput(2))

img = img[s[1]:e[1],s[0]:e[0]]
img = 2.0*img[:,:,1] - img[:,:,0]-img[:,:,-1]
img = np.uint8( 255*(img-img.min())/(img.max()-img.min()))
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img)
#%%

normalize = lambda x: (x-x.min() ) / (x.max()-x.min())




imBlur = cv2.GaussianBlur(img,(11,11),9)
plt.imshow(imBlur)
imBlurNormalized = normalize(imBlur)


laplacian = cv2.Laplacian(imBlurNormalized ,cv2.CV_64F,ksize=31)


laplacian = np.uint8(255*normalize(laplacian))
lp = cv2.GaussianBlur(laplacian,(7,7),5)
lShape = lp.shape



plt.figure()
plt.imshow(lp)


#%%
#verticalLine   = getLineImg(lShape[0], 'v')
#horizontalLine = getLineImg(lShape[1], 'h')



rotaciones = np.arange(-5,5,.1)


#horizontalDict = findBestDirection(lp,rotaciones, verticalConv,
#								   horizontalLine, 11)
#verticalDict= findBestDirection(lp,rotaciones, horizontalConv,
#								verticalLine,11)


horizontalDict,verticalDict = imgTools.findLines(lp,11,11,rotaciones)



plt.figure()
plt.subplot(1,2,1)
plt.imshow(horizontalDict['img'])
plt.subplot(1,2,2)
plt.imshow(verticalDict['img'])

plt.figure()
plt.subplot(2,1,1)
plt.plot(horizontalDict['convRes'])
plt.plot(horizontalDict['peaks'], 
		 horizontalDict['convRes'][horizontalDict['peaks']],'+r')
plt.subplot(2,1,2)
plt.plot(verticalDict['convRes'])
plt.plot(verticalDict['peaks'], 
		 verticalDict['convRes'][verticalDict['peaks']],'+r')



#lineImgH = np.copy(horizontalDict['img'])
#lineImgV = np.copy(verticalDict['img'])
lineImgH = np.zeros_like(horizontalDict['img'])
lineImgV = np.zeros_like(verticalDict['img'])
imShape = lineImgH.shape


lw = 2

for i,p in enumerate(horizontalDict['peaks']):
	cv2.line(lineImgH,(0,p),(lShape[1],p),255,lw)
	
for i,p in enumerate(verticalDict['peaks']):
	cv2.line(lineImgV,(p,0),(p,lShape[0]),255,lw)

plt.figure('horizontal')
plt.subplot(1,2,1)
plt.imshow(horizontalDict['img'])
plt.subplot(1,2,2)
plt.imshow(lineImgH)

plt.figure('vertical')
plt.subplot(1,2,1)
plt.imshow(verticalDict['img'])
plt.subplot(1,2,2)
plt.imshow(lineImgV)


plt.figure()
plt.subplot(121)
plt.imshow(horizontalDict['img']*(255-lineImgH)/255 + lineImgH/255)
plt.subplot(122)
plt.imshow(verticalDict['img']*(255-lineImgV)/255 + lineImgV/255)

"""HAY QUE CHECKEAR ESTA FUNCION NO SE SI ESTA ANDANDO BIEN"""
qq = imgTools.crearImagenDeLineas(lp.shape,
						 verticalDict['peaks'], verticalDict['rotVal'],
						 horizontalDict['peaks'], horizontalDict['rotVal'])

estoTieneQueAndar = lp *((255-qq)/255) + qq
plt.figure()
plt.imshow(estoTieneQueAndar )

