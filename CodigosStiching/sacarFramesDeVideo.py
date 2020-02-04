import numpy as np
import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip 

ffmpeg_extract_subclip("video1.mp4", t1, t2, targetname="test.mp4")


cap = cv2.VideoCapture("CUT1.mp4")
count=0
succes=True

while(succes):
    cap.set(cv2.CAP_PROP_POS_MSEC,(count*500))
    succes,image=cap.read()
    image_last=cv2.imread("frame{}.jpg".format(count-1))
    if np.array_equal(image,image_last):
        break
    cv2.imwrite('frame%d.jpg' % count , image)
    count+=1

#cap = cv2.VideoCapture(0)
#print(cap.isOpened())
#ret,frame = cap.read()
#gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (21, 21), 0)
#fondo=gray
#
#a1=0.1
#
#for i in range (1,100):
#    ret,frame = cap.read()
#    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    gray = cv2.GaussianBlur(gray, (21, 21), 0)
#    fondo=(fondo*a1+(1-a1)*gray)
#
#a=.999
#
#while(1):
#    
#    ret,frame = cap.read()
#    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    gray = cv2.GaussianBlur(gray, (21, 21), 0)
#    #fondo=(fondo*a+(1-a)*gray)
#    objeto=np.abs(fondo-gray)
#    objeto=np.uint8(objeto)
#    objeto= cv2.threshold(objeto,1,255, cv2.THRESH_BINARY)[1]
#    cv2.imshow('objeto', objeto)
#    fondo1=np.uint8(fondo)
#    cv2.imshow('fondo', fondo1)
#
#    if cv2.waitKey(1) & 0xFF==ord('q'):
#        break
#    time.sleep(0.015)
#
#cap.release()
#cv2.destroyAllWindows()
#
