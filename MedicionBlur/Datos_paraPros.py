#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:30:13 2019

@author: braso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

data= np.load("/home/braso/Agricultura_UNQ/MedicionBlur/blur_allvideos.npy",allow_pickle=True)
vels=np.load("list_Vel.npy")
heights=np.load("list_Height.npy")
