
import cv2
import glob
import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt

"""
#******************************************************
# DETECCION Y GRAFICA DE ESQUINAS
#******************************************************
Codigo para calibración de la camara del drone.
#*****************************************************************"""
#%%
def generateCorners(folder,patternSize=(9,6),imageSize=(3840,2160)):
	#patternSize = (9, 6) # los cuadraditos del chessboard -1
	#imageSize = (3840,2160) # Tiene que ser el tamaño de las imagenmes 
	
	images = glob.glob(folder+"*.png")
	images.sort()


	di = dict()
	for idx,strfile in enumerate(images):
		print(idx,' de ',len(images))
		img = cv2.imread(strfile, cv2.IMREAD_GRAYSCALE) # Lee una imagen en escala de grises
		found, corners = cv2.findChessboardCorners(img, patternSize)
		if found:
			print(strfile+' Good')
			di[idx] = (corners,strfile)
	
	np.save(folder + 'CornersEnImagenes.npy',di)




 # Leo todas las imagenes de la carpeta
#images = glob.glob(r"C:\Users\BraianSoullier\Desktop\TAMIUSOULLIER\SCRIPS\CalibrateCamera\*.png")

#folder = 'calibracion_1_240/'

folders = glob.glob('*/')
folders.sort()
for f in folders:
	print(f)
	generateCorners(f)





#%%


# for i in range(20):
# 	print(i)
# 	imgs = np.random.choice(images,30)
# 	corners = ()
# # Se arma un vector con la identificacion de cada cuadrito
# 	objp = np.zeros((6*9,3), np.float32)
# 	objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2) #rellena las columnas 1 y 2


# 	# Arrays para almacenar los puntos de los objetos y los puntos de las imagenes .
# 	objpoints = [] # puntos 3D en el mundo real
# 	imgpoints = [] # puntos 2D en el plano de la imagen


# 	# Encuentro corners en las imagenes
# 	for strfile in imgs:
# 		img = cv2.imread(strfile, cv2.IMREAD_GRAYSCALE) # Lee una imagen en escala de grises
# 		found, corners = cv2.findChessboardCorners(img, patternSize)
# 		if found:
# 			print(strfile+' Good')
# 			imgpoints.append(corners)
# 			objpoints.append(objp)
# 		else:
# 			print(strfile + ' Bad')
# 	


# 	rvecs = ()
# 	tvecs = ()
# 	cameraMatrix = ()
# 	distCoeffs =()


# 	#flags =cv2.CALIB_ZERO_TANGENT_DIST+ cv2.CALIB_FIX_K1+ cv2.CALIB_FIX_K2+ cv2.CALIB_FIX_K3+cv2.CALIB_FIX_PRINCIPAL_POINT
# 	flags=0

# 	rms, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, 
# 																   imgpoints, imageSize, cameraMatrix,
# 																   distCoeffs, rvecs, tvecs, flags)

# 	dic = {'cameraMatrix':cameraMatrix,'distCoeffs':distCoeffs,'rvecs':rvecs,'tvecs':tvecs}
# 	np.save('/home/braso/Agricultura_UNQ/CalibrateCamera/calibracion_1_240/CP_dist'+str(i),dic)
#np.save('C:/Users/BraianSoullier/Desktop/TAMIUSOULLIER/SCRIPS/CorrecDeDist/usbCamPars.npy',dic)