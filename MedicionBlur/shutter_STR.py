#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:14:12 2019

@author: braso
"""


import pandas as pd
import numpy as np
import glob
from time import time


files=glob.glob("/home/braso/Escritorio/Videos calib 191113/*.SRT")
files.sort()
shutters=[]
for file in files:
    fil=open(file)
    subt=fil.read().split('\n\n')
    l=subt[0].split("[")
    shutter=(l[2].split(':')[1].replace("]"," "))[1:6]
    shutters.append(shutter)

np.save("shutters.npy",shutters)