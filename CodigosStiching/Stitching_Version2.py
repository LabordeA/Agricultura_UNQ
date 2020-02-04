# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:40:02 2019

@author: Braso
"""

import numpy           as np
import matplotlib.pyplot as plt
import cv2
from glob import glob

surf = cv2.xfeatures2d.SURF_create(2000)


folder = "/home/braso/Agricultura_UNQ/CodigosStiching/Frames/*.jpg"
files =glob(folder)
files.sort()

#imgs = { "frame0.jpg":[],"frame1.jpg":[],"frame2.jpg":[],"frame3.jpg":[],"frame4.jpg":[],"frame5.jpg":[] }

img=list()

for file in files:
    print()
    img.append(cv2.imread(file))

bf = cv2.BFMatcher() # Creo objeto BFMatcher
(kp0,des0)=surf.detectAndCompute(img[0],None)
kpOld=kp0
desOld=des0
H_ac=np.eye(3)
stit=[]
stit.append(img[0])
for i in range(1,len(img)):
    kp, des = surf.detectAndCompute(img[i],None) # Saco descriptores en segunda imagen
    matches = bf.knnMatch(des,desOld, k=2)  # Hago los matches de los des1 y des2 
    # Realizo selección de matches de descriptores
    good = []
    for m in matches:
        if m[0].distance < 0.4*m[1].distance:
            good.append(m)
            matches = np.asarray(good)

    if len(matches[:,0]) >= 4:
        src = np.float32([ kp[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
        dst = np.float32([ kpOld[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
        p1 = src.transpose(1,2,0)[0]
        p2 = dst.transpose(1,2,0)[0]
        H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
        H_ac=np.dot(H,H_ac)
    else:
        raise RuntimeError ('Error Faltan Keypoints')

    dst = cv2.warpPerspective(img[i],H_ac,(np.uint64(stit[i-1].shape[1]+H_ac[0,2]),np.uint64(stit[i-1].shape[0]-H_ac[1,2])))
    plt.figure()
    plt.imshow(dst)
    plt.title('Warped Image')
#   dst[0:stit[i-1].shape[0], 0:stit[i-1].shape[1]] = stit[i-1]
    aux=np.zeros(dst.shape, dtype=np.uint8)
#    stit[i-1]=stit[i-1]+aux
    aux[:stit[i-1].shape[0], :stit[i-1].shape[1]] =  stit[i-1]
    mask = np.any(dst != 0, axis=2)
    Kernel=np.ones([3,3],dtype=np.uint8)
    mask=np.uint8(mask)
    mask=cv2.erode(mask,Kernel) != 0
    aux[mask] = dst[mask]
    stit.append(aux)
    
    plt.figure()
    plt.imshow(stit[i][:,:,::-1])
    plt.title('Stitching')
    kpOld=kp
    desOld=des
    
    