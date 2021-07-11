# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:27:07 2020

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:18:44 2020

@author: hp
"""


#import numpy as np
import cv2
import serial
import time
#import pyserial


ser = serial.Serial('COM3', 9600, timeout=1)
#ser1 = serial.Serial('COM16', 9600, timeout=1)
#ser2 = serial.Serial('COM16', 9600, timeout=1)


face_cascade = cv2.CascadeClassifier(r'C:\Users\Varun\Desktop\HaarHand\OpenCV\haarcascades\face.xml')
fist_cascade = cv2.CascadeClassifier(r'C:\Users\Varun\Desktop\HaarHand\OpenCV\haarcascades\hand.xml')
palm_cascade = cv2.CascadeClassifier(r'C:\Users\Varun\Desktop\HaarHand\OpenCV\haarcascades\palm.xml')

cap = cv2.VideoCapture(0)
while (cap):
      _, img = cap.read()

      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      fist = fist_cascade.detectMultiScale(gray, 1.3, 5)
      palm = palm_cascade.detectMultiScale(gray, 1.3, 5)
      
     #if  any(faces):
      for (x,y,w,h) in faces:
              img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
              ser.write('f'.encode())
              print('1')
            #  time.sleep(1)
             
      for (ex,ey,ew,eh) in fist:
          img = cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
          ser.write('h'.encode())
          print('2')
          #time.sleep(1)
          
     
      for (mx,my,mw,mh) in palm:
          img = cv2.rectangle(img,(mx,my),(mx+mw,my+mh),(0,0,255),2)
          ser.write('p'.encode())
          print('3') 
          #time.sleep(1)
      
    
      #ser.close()
         
      cv2.imshow('img',img) 
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
cap.release()
cv2.destroyAllWindows()