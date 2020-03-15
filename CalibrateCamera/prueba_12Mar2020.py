#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:29:30 2020

@author: ulises
"""


import numpy as np
import matplotlib.pyplot as plt
import cv2
from glob import glob

path="/home/braso/Agricultura_UNQ/CalibrateCamera/cal*/"

files = glob(path+'Corne*.npy')

for j in range(0,4):
	print(j)
	data = np.load(files[j],allow_pickle=True).item()
	plt.figure(files[j])
	for i in data.values():
		plt.plot(*i[0][:,0,:].T,'+')
