#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:46:49 2019

@author: braso
"""

# %% Comparacion graficas en el mismo shutter
import cv2
import matplotlib.pyplot as plt
import numpy

path='/home/braso/Agricultura_UNQ/MedicionBlur/'
folder1='4m_1ms_240
# Cargo rusticamente las areas de los shutters a 240
area1=np.load(path+'areas.npy',allow_pickle=True)
