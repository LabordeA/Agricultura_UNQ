#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:30:00 2019

@author: nicolascuedo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
path="/home/nicolascuedo/Escritorio/TAMIU_Octubre/SCRIPS/Hough/"
#file= "/campoCortado.jpg"
#file= "/frame4.jpg"
file="/GI.jpg"
#file="/santiago.jpg"
file2="/RGB.jpg"

img1 = cv2.imread(path+file2,cv2.IMREAD_GRAYSCALE)

img=cv2.imread(path+file, cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(img)


ret, thresh = cv2.threshold(img1,90,255,0)
#thresh= np.uint8(255*(thresh-thresh.min()) / (thresh.max()-thresh.min()))


kernel=np.ones(5)
thresh=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
#thresh=cv2.GaussianBlur(thresh,(5,5),cv2.BORDER_DEFAULT)

#thresh=cv2.
plt.figure('Campo de cultivo')
plt.imshow(thresh,'gray')

img=thresh
#img = abs(thresh-255)
# %%
# Para una simulacion mala, comentar if y ejecutar cv2.HL con 300

img1 = cv2.imread(path+file2)


#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray,50,150,apertureSize = 3)

black=np.zeros(img1.shape)

# Find lines of field and Draw it in red color
lines = cv2.HoughLines(img,1,np.pi/180,200)
if lines is not None:
	for line in lines:
		for rho,theta in line:
			if (0<=theta<=0.01 or (np.pi/2)-0.01<=theta<=(np.pi/2)+0.01):
			    a = np.cos(theta)
			    b = np.sin(theta)
			    x0 = a*rho
			    y0 = b*rho
			    x1 = int(x0 + 1000*(-b))
			    y1 = int(y0 + 1000*(a))
			    x2 = int(x0 - 1000*(-b))
			    y2 = int(y0 - 1000*(a))
			
			    cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),5)
			    cv2.line(black,(x1,y1),(x2,y2),(255,255,255),10)
			    plt.figure('RGB hough')
			    plt.imshow(img1[:,:,::-1])
			    plt.figure('scatter')
			    plt.scatter(rho,theta)

plt.xlabel('rho')
plt.ylabel('theta')
plt.title('Hough Space')
cv2.imwrite('testRGB.jpg',img1)
cv2.imwrite('lineas.jpg',black)

plt.figure()
plt.imshow(img1[:,:,::-1])
plt.title('Ground lines detection')



black=np.uint8(black)
black=cv2.cvtColor(black,cv2.COLOR_RGB2GRAY)
ret, black = cv2.threshold(black,127,255,0)
black=np.uint8(black/255)
black=abs(black-1)
plt.imshow(black)

contoursImg=np.ones(img1.shape)
imgC,cnt,hr=cv2.findContours(black,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(contoursImg,cnt,-1,(0,0,0))
contoursImg=np.uint8(contoursImg)
contoursImg=cv2.cvtColor(contoursImg,cv2.COLOR_RGB2GRAY)
plt.imshow(contoursImg)



ret, labels = cv2.connectedComponents(contoursImg)


def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue==0] = 0

    cv2.imshow('labeled.png', labeled_img)
    cv2.waitKey()

imshow_components(labels)

# %%
ret, labels = cv2.connectedComponents(black)

def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue==0] = 0

    cv2.imshow('labeled.png', labeled_img)
    cv2.waitKey()

imshow_components(labels)

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()
 
# Detect blobs.
keypoints = detector.detect(black)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(black, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

# %% Prueba Bra
img1 = cv2.imread(path+file2)
lines = cv2.HoughLines(img,1,np.pi/180,200)
if lines is not None:
	plt.figure()
	for line in lines:
		for rho,theta in line:
			if (0<=theta<=0.01 or (np.pi/2)-0.01<=theta<=(np.pi/2)+0.01):
				a = np.cos(theta)
				b = np.sin(theta)
				x0 = a*rho
				y0 = b*rho
				x1 = int(x0 + 1000*(-b))
				y1 = int(y0 + 1000*(a))
				x2 = int(x0 - 1000*(-b))
				y2 = int(y0 - 1000*(a))
				cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),2)
				plt.scatter(rho,theta)

#    for line in lines:
#        for x1,y1,x2,y2 in line:
#            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

plt.figure()
plt.imshow(img1[:,:,::-1])
#plt.figure()
#plt.scatter(lines[:,0,0],lines[:,0,1])


