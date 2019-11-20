# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:46:10 2019

@author: BraianSoullier
"""

import cv2
import numpy as np
import time 
import matplotlib.pyplot as plt 
from glob import glob
import pandas as pd 

#start_time = time.time()
videos=glob("/home/braso/Escritorio/Videos calib 191113/*.MP4")
videos.sort()
subtitulos=glob(("/home/braso/Escritorio/Videos calib 191113/*.SRT"))
subtitulos.sort()
files=glob("/home/braso/Escritorio/Videos calib 191113/FligthRecord/*.csv")
strings=np.load("shutters.npy")
dt_frame1= pd.read_csv(files[0],encoding = "ISO-8859-1")
dt_frame2= pd.read_csv(files[1],encoding = "ISO-8859-1")
dt_frame=pd.concat([dt_frame1,dt_frame2])

dt_frame['CUSTOM.updateTime'] = pd.to_datetime(dt_frame['CUSTOM.updateTime'])+pd.offsets.Hour(-3)

def createDataFramesubt(subt):
	subt = subt.split('\n\n')
	df_subt = pd.DataFrame(columns = ['frameNumber','dateTime','lat','lon'])
	for i in range(len(subt)):
		l 			= subt[i].split('[')
		if l[0] != '':
			l0sp 		= l[0].split('\n')
			datetime 	= ','.join(l0sp[-2].split(',')[:-1])
			frNum 		= np.int32(l0sp[2].split(':')[1].split(',')[0])
			la 			= l[-2].replace(']','').replace(' ','').split(':')[-1]
			lo 			= l[-1].replace(']','').replace(' ','').split(':')[-1].replace('</font>','')
			df_subt = df_subt.append({'frameNumber':frNum,
							 'dateTime':pd.to_datetime(datetime),
							 'lat':np.float(la),
							 'lon':np.float(lo)},ignore_index=True)
	return df_subt



# %%   Ver todo los videos con el umbral del patron
for counter,file in enumerate(videos):
    #dt_log=dt_frame
    cap = cv2.VideoCapture(file)
    subt=subtitulos[counter]
    subt_abierto=open(subt).read()
    dt_subt=createDataFramesubt(subt_abierto)
    
    dt_log = dt_frame[dt_frame['CUSTOM.updateTime']> dt_subt['dateTime'].iloc[0]]
    dt_log = dt_log[dt_log['CUSTOM.updateTime']< dt_subt['dateTime'].iloc[-1]]
    
    measurementsIdxon_df_log = (dt_log['GIMBAL.pitch']<-85)
    starts = np.argwhere((1*measurementsIdxon_df_log).diff()>0)
    starts = starts  if len(starts )>0 else [[0]]
    ends   = np.argwhere((1*measurementsIdxon_df_log).diff()<0)
    ends = ends  if len(ends )>0 else [[-1]]
    tstart = dt_log.iloc[starts[0]]['CUSTOM.updateTime']
    tend   = dt_log.iloc[ends[0]]['CUSTOM.updateTime']
    starts=np.argmin(np.abs(dt_subt['dateTime'].values - tstart.values))
    ends=np.argmin(np.abs(dt_subt['dateTime'].values - tend.values))
    print("Archivo=",file)
    if(strings[counter]=="1/60."):
        umbral=190
    if(strings[counter]=="1/120"):
        umbral=150
    if(strings[counter]=="1/240"):
        umbral=110
    if(strings[counter]=="1/160"):
        umbral=110
    print("umbral",umbral)
    print("Counter",counter)
    cap.set(cv2.CAP_PROP_POS_FRAMES,starts+40)
    cont=starts
    while(cap.isOpened()):
        ret, frame = cap.read()
        cont+=1
        if (cont==ends):
            break
        if(ret!=False):
            img=cv2.resize(frame,(1240,640))
            cv2.imshow('frame',img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',img)
            ja,imgB=cv2.threshold(gray,umbral,255,cv2.THRESH_BINARY)
            kernel=np.array(([0,1,0],[1,1,1],[0,1,0]),np.uint8)
            imgB=cv2.morphologyEx(imgB,cv2.MORPH_OPEN,kernel)
            imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(imgB,cnt,-1,(127,0,0),5)
            cv2.imshow("Contorno",imgB)
            print('\r' , cap.get(cv2.CAP_PROP_POS_FRAMES),end='')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            cap.release()
    cap.release()
    cv2.destroyAllWindows()


qq# %%
LapALL=[]
for vid in videos :
    cap = cv2.VideoCapture(vid)
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
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    LapALL.append(Laplacian)
    cap.release()
    cv2.destroyAllWindows()


#end_time= time.time()
#
#print("Elapsed time: %.10f seconds." % (end_time - start_time))




# %% Buscando el patron de puntos para hacer una mascara y calcular el laplaciano solo donde aparece el patron
file=videos[28]
cap = cv2.VideoCapture(file)
#cap.set(cv2.CAP_PROP_POS_FRAMES,570)
while(cap.isOpened()):
    ret, frame = cap.read()
    img=cv2.resize(frame,(1240,640))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray=cv2.resize(gray,(1240,640))
#    cv2.imshow('frame',img)
#    ja,imgB=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
#    ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,2001,2)
    th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,2001,2)
    cv2.imshow("C1",th2)
    cv2.imshow("C2",th3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()




#
#    kernel=np.array(([0,1,0],[1,1,1],[0,1,0]),np.uint8)
#    imgB=cv2.morphologyEx(imgB,cv2.MORPH_OPEN,kernel)


#plt.figure()
#plt.imshow(imgB)
#
#
#imgC,cnt,hr=cv2.findContours(imgB,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
##cv2.fillPoly(imgB,cnt,255)
#cv2.drawContours(imgB,cnt,-1,(127,0,0))
#plt.figure()
#plt.imshow(imgB)
#
#
#qq