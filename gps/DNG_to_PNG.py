# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import rawpy 
from glob import glob
import cv2

fotos=glob("/home/braso/Escritorio/Videos calib 191113/*.DNG")

for i in fotos :
    fot=rawpy.imread(i).postprocess()
    cv2.imwrite(i.split('.')[0]+'.png',fot)    