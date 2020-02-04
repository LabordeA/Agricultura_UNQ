# HASTA AHORA ESTE ES EL QUE MEJOR FUNCIONA!!!!!

# Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame1.jpg")

# Importacion de imagenes
img = cv2.imread(r'D:\Facultad\TAMIU\CodigosStiching\frame0.jpg')

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2)  # Hago los matches de los des1 y des2 

# Realizo selección de matches de descriptores
good = []
for m in matches:
    if m[0].distance < 0.4*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src,dst y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)

# Creo matriz de rototranslasion A
#p1 = src.transpose(1,2,0)[0]
#p2 = dst.transpose(1,2,0)[0]
#f1=p1.transpose()
#f2=p2.transpose()
#fil, col=f2.shape
#F2=np.concatenate([f2.transpose(),np.ones([1,fil])])
#A=np.dot(f1.transpose(),np.linalg.pinv(F2))

# Pego la segunda imagenes rototransladada
#dst = cv2.warpPerspective(img_,H,(img.shape[1] + img_.shape[1]-1500, img.shape[0]))
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))


# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img

cv2.imwrite("D:\Facultad\TAMIU\CodigosStiching\output0.jpg",dst)
plt.imshow(dst)
plt.show()

# %%

# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame2.jpg")
#img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)

# Importacion de imagenes
img = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\output0.jpg")
#img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2) # # Hago los matches de los des1 y des2 

# Realizo match de descriptores
good = []
for m in matches:
    if m[0].distance < 0.4*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src,dstt y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)

# Creo matriz de rototranslasion A
#p1 = src.transpose(1,2,0)[0]
#p2 = dst.transpose(1,2,0)[0]
#f1=p1.transpose()
#f2=p2.transpose()
#fil, col=f2.shape
#F2=np.concatenate([f2.transpose(),np.ones([1,fil])])
#A=np.dot(f1.transpose(),np.linalg.pinv(F2))

# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))
#dst = cv2.warpAffine(img1,A,(img.shape[1] + img1.shape[1], img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img
cv2.imwrite("D:\Facultad\TAMIU\CodigosStiching\output1.jpg",dst)
plt.imshow(dst)
plt.show()


# %%

# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame3.jpg")
#img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)

# Importacion de imagenes
img = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\output1.jpg")
#img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2) # # Hago los matches de los des1 y des2 

# Realizo match de descriptores
good = []
for m in matches:
    if m[0].distance < 0.4*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src,dstt y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)

# Creo matriz de rototranslasion A
#p1 = src.transpose(1,2,0)[0]
#p2 = dst.transpose(1,2,0)[0]
#f1=p1.transpose()
#f2=p2.transpose()
#fil, col=f2.shape
#F2=np.concatenate([f2.transpose(),np.ones([1,fil])])
#A=np.dot(f1.transpose(),np.linalg.pinv(F2))

# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))
#dst = cv2.warpAffine(img1,A,(img.shape[1] + img1.shape[1], img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img
cv2.imwrite("D:\Facultad\TAMIU\CodigosStiching\output2.jpg",dst)
plt.imshow(dst)
plt.show()


# %%

# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame4.jpg")
#img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)

# Importacion de imagenes
img = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\output2.jpg")
#img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2) # # Hago los matches de los des1 y des2 

# Realizo match de descriptores
good = []
bra=0
for m in matches:
    bra=bra+1
    if m[0].distance < 0.7*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src,dstt y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)

# Creo matriz de rototranslasion A
#p1 = src.transpose(1,2,0)[0]
#p2 = dst.transpose(1,2,0)[0]
#f1=p1.transpose()
#f2=p2.transpose()
#fil, col=f2.shape
#F2=np.concatenate([f2.transpose(),np.ones([1,fil])])
#A=np.dot(f1.transpose(),np.linalg.pinv(F2))

# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))
#dst = cv2.warpAffine(img1,A,(img.shape[1] + img1.shape[1], img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img
cv2.imwrite("D:\Facultad\TAMIU\CodigosStiching\output3.jpg",dst)
plt.imshow(dst)
plt.show()



# %%

# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame5.jpg")
#img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)

# Importacion de imagenes
img = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\output3.jpg")
#img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2) # # Hago los matches de los des1 y des2 

# Realizo match de descriptores
good = []
for m in matches:
    if m[0].distance < 0.75*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src,dstt y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)

# Creo matriz de rototranslasion A
#p1 = src.transpose(1,2,0)[0]
#p2 = dst.transpose(1,2,0)[0]
#f1=p1.transpose()
#f2=p2.transpose()
#fil, col=f2.shape
#F2=np.concatenate([f2.transpose(),np.ones([1,fil])])
#A=np.dot(f1.transpose(),np.linalg.pinv(F2))

# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))
#dst = cv2.warpAffine(img1,A,(img.shape[1] + img1.shape[1], img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img
cv2.imwrite(r"D:\Facultad\TAMIU\CodigosStiching\output4.jpg",dst)
plt.imshow(dst)
plt.show()



# %%

# Importacion de imagenes
img_ = cv2.imread('frame5.jpg')
#img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)

# Importacion de imagenes
img = cv2.imread('output4.jpg')
#img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2) # # Hago los matches de los des1 y des2 

# Realizo match de descriptores
good = []
for m in matches:
    if m[0].distance < 0.4*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src,dstt y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)

# Creo matriz de rototranslasion A
#p1 = src.transpose(1,2,0)[0]
#p2 = dst.transpose(1,2,0)[0]
#f1=p1.transpose()
#f2=p2.transpose()
#fil, col=f2.shape
#F2=np.concatenate([f2.transpose(),np.ones([1,fil])])
#A=np.dot(f1.transpose(),np.linalg.pinv(F2))

# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))
#dst = cv2.warpAffine(img1,A,(img.shape[1] + img1.shape[1], img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img
cv2.imwrite('output5.jpg',dst)
plt.imshow(dst)
plt.show()



