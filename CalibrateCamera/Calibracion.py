
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
		print('\r',idx,' de ',len(images),sep='')
		img = cv2.imread(strfile, cv2.IMREAD_GRAYSCALE) # Lee una imagen en escala de grises
		found, corners = cv2.findChessboardCorners(img, patternSize)
		if found:
			print('\r\t',strfile+' Good',sep='')
			di[idx] = (corners,strfile)
	print('\n')
	np.save(folder + 'CornersEnImagenes.npy',di)




 # Leo todas las imagenes de la carpeta
#images = glob.glob(r"C:\Users\BraianSoullier\Desktop\TAMIUSOULLIER\SCRIPS\CalibrateCamera\*.png")

#folder = 'calibracion_1_240/'

folders = glob.glob('*/')
folders.sort()

findCuerners =False
"""si quiero encontrar los corners cambioeste flag, sino los cargo"""
if findCuerners:
	for f in folders:
		print(f)
		generateCorners(f)

cuerners = []
for f in folders:
	aux = np.load(f + 'CornersEnImagenes.npy',allow_pickle=True).item()
	cuerners.append(aux)



#%%
	
#folderOfInterest ='calibracion_1_240/'

patternSize=(9,6)
imageSize=(3840,2160)

# Se arma un vector con la identificacion de cada cuadrito
objp 		= np.zeros((6*9,3), np.float32)
objp[:,:2] 	= np.mgrid[0:9, 0:6].T.reshape(-1, 2) #rellena las columnas 1 y 2

nReals=20
for folderOfInterest in folders:

	fIndex = np.where([folderOfInterest==f for f in folders])[0][0]
	
	for i in range(nReals):
		print('\r Realización: {:d} de {:d}'.format(i,nReals),end='')
		corners 		= cuerners[fIndex]
		lc 			= len(corners)
		keys 		= [c for c in corners.keys()]
		choices 		= np.random.choice(keys,np.int(lc/2))
		imgpoints 	= [corners[c][0] for c in choices]



	
		objpoints = []
		for tp in imgpoints:
			objpoints.append(objp)

	
		rvecs 			= ()
		tvecs 			= ()
		cameraMatrix 	= ()
		distCoeffs 		= ()
	
		flags 		= 0
		returnKeys 	= ['rms','cameraMatrix','distCoeffs','rvecs','tvecs']
		returns 		= cv2.calibrateCamera(	objpoints, imgpoints, imageSize, 
											cameraMatrix, distCoeffs, rvecs, 
											tvecs, flags)
		
		
		dic = dict()
		for key,val in zip(returnKeys,returns):
			dic[key]= val 
		np.save(folderOfInterest + 'CP_dist'+str(i),dic)
	print('\r\n \t\t Saved At: {:s}'.format(folderOfInterest.strip('/')) )
	#np.save('./CorrecDeDist/usbCamPars.npy',dic)