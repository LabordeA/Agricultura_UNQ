#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:56:55 2019

@author: nicolascuedo
"""

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
file="/GI_2.jpg"
#file="/santiago.jpg"
file2="/RGB_2.jpg"

img1 = cv2.imread(path+file2,cv2.IMREAD_GRAYSCALE)

img=cv2.imread(path+file, cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(img)


ret, thresh = cv2.threshold(img1,100,255,0) # 90 es el que va
#thresh= np.uint8(255*(thresh-thresh.min()) / (thresh.max()-thresh.min()))


kernel=np.ones(3)
thresh=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
thresh=cv2.GaussianBlur(thresh,(5,5),cv2.BORDER_DEFAULT)
thresh=cv2.morphologyEx(thresh,cv2.MORPH_DILATE,kernel)

#thresh=cv2.
plt.figure('Campo de cultivo')
plt.imshow(thresh,'gray')

img=thresh
#img = abs(thresh-255)
# %%
img1 = cv2.imread(path+file2)


#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray,50,150,apertureSize = 3)


# Find lines of field and Draw it in red color
lines = cv2.HoughLines(img,0.8,np.pi/180,500)
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
				
cv2.imwrite('testRGB.jpg',img1)

plt.figure()
plt.imshow(img1[:,:,::-1])

# %% Prueba Bra
rho_old=0
tol=10
lines = cv2.HoughLines(img,1,np.pi/180,400)
if lines is not None:
	plt.figure()
	for line in lines:
		for rho,theta in line:
			if (0<=theta<=0.01 and (rho-rho_old)>tol): #or (np.pi/2)-0.01<=theta<=(np.pi/2)+0.01
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
			    rho_old=rho

plt.figure()
plt.imshow(img1[:,:,::-1])
#plt.figure()
#plt.scatter(lines[:,0,0],lines[:,0,1])
