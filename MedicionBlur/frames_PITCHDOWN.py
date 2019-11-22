#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:11:35 2019

@author: braso
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

# %%
Prin=[]
Fin=[]
for counter in range(len(subtitulos)):
    subt=subtitulos[counter]
    subt_abierto=open(subt).read()
    dt_subt=createDataFramesubt(subt_abierto)
    
    dt_log = dt_frame[dt_frame['CUSTOM.updateTime']> dt_subt['dateTime'].iloc[0]]
    dt_log = dt_log[dt_log['CUSTOM.updateTime']< dt_subt['dateTime'].iloc[-1]]
    measurementsIdxon_df_log = (dt_log['GIMBAL.pitch']<-85)
    starts = np.argwhere((1*measurementsIdxon_df_log).diff()>0)
    starts = starts  if len(starts) > 0 else [[0]]
    ends   = np.argwhere((1*measurementsIdxon_df_log).diff()<0)
    ends = ends  if len(ends )>0 else [[-1]]
    tstart = dt_log.iloc[max(starts)]['CUSTOM.updateTime']
    tend   = dt_log.iloc[max(ends)]['CUSTOM.updateTime']
    starts=np.argmin(np.abs(dt_subt['dateTime'].values - tstart.values))
    ends=np.argmin(np.abs(dt_subt['dateTime'].values - tend.values))
    Prin.append(starts)
    Fin.append(ends)

np.save('/home/braso/Agricultura_UNQ/MedicionBlur/starts.npy',Prin)
np.save('/home/braso/Agricultura_UNQ/MedicionBlur/ends.npy',Fin)
