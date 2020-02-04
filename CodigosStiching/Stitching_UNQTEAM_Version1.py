# ATENCIÓN, CORRER EL CÓDIGO POR SECCIONES, YA QUE LAS SUBSIGUIENTES SECCIONES
# UTILIZAN INFORMACIÓN DE SECCIONES ANTERIORES. Todavia no se realizo un bucle 
# para esto. 

# Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame1.jpg")

# Importacion de imagenes
img = cv2.imread(r'D:\Facultad\TAMIU\CodigosStiching\frame0.jpg')

imShape =img_.shape #Shape de la imagen  

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

# Genero matrices src, dst y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    
    p1 = src.transpose(1,2,0)[0]
    p2 = dst.transpose(1,2,0)[0]
    
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)

#Key points SURF
plt.figure()
plt.imshow(np.vstack((img_,img)))
plt.plot([p1[0],p2[0]],[p1[1] ,p2[1]+imShape[0]],'r',linewidth=3,alpha=.3)

# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img

#Guardo imagenes compuestas
cv2.imwrite("D:\Facultad\TAMIU\CodigosStiching\output0.jpg",dst)
plt.imshow(dst)
plt.show()
# %%
# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame2.jpg")

# Importacion de imagenes
img = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\output0.jpg")

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2) # # Hago los matches de los des1 y des2 

# Realizo selección de matches de descriptores
good = []
for m in matches:
    if m[0].distance < 0.4*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src, dst y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img

#Guardo composición
cv2.imwrite("D:\Facultad\TAMIU\CodigosStiching\output1.jpg",dst)
plt.imshow(dst)
plt.show()

# %%
# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame3.jpg")

# Importacion de imagenes
img = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\output1.jpg")

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2) # # Hago los matches de los des1 y des2 

# Realizo selección de matches de descriptores
good = []
for m in matches:
    if m[0].distance < 0.4*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src, dst y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img

#Guardo composición
cv2.imwrite("D:\Facultad\TAMIU\CodigosStiching\output2.jpg",dst)
plt.imshow(dst)
plt.show()

# %%
# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame4.jpg")

# Importacion de imagenes
img = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\output2.jpg")

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2) # # Hago los matches de los des1 y des2 

# Realizo selección de matches de descriptores
good = []
for m in matches:
    if m[0].distance < 0.7*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src, dst y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img

#Guardo composición
cv2.imwrite("D:\Facultad\TAMIU\CodigosStiching\output3.jpg",dst)
plt.imshow(dst)
plt.show()

# %%
# Importacion de imagenes
img_ = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\frame5.jpg")

# Importacion de imagenes
img = cv2.imread(r"D:\Facultad\TAMIU\CodigosStiching\output3.jpg")

# Creacion de objeto SURF
surf = cv2.xfeatures2d.SURF_create()

#for surf
kp1, des1 = surf.detectAndCompute(img_,None) # Saco descriptores en primera imagen
kp2, des2 = surf.detectAndCompute(img,None) # Saco descriptores en segunda imagen
bf = cv2.BFMatcher() # Creo objeto BFMatcher
matches = bf.knnMatch(des1,des2, k=2) # # Hago los matches de los des1 y des2 

# Realizo selección de matches de descriptores
good = []
for m in matches:
    if m[0].distance < 0.75*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# Genero matrices src, dst y H
if len(matches[:,0]) >= 4:
    src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
# Pego la segunda imagenes rototransladada
dst = cv2.warpPerspective(img_,H,(img.shape[1] + np.uint8(H[0,2]), img.shape[0]))

# Ploteo imagenes warpeadas
plt.figure()
plt.imshow(dst)
plt.title('Warped Image')

plt.figure()
dst[0:img.shape[0], 0:img.shape[1]] = img

#Guardo composición
cv2.imwrite("D:\Facultad\TAMIU\CodigosStiching\output4.jpg",dst)
plt.imshow(dst)
plt.show()
