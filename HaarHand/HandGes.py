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


import numpy as np
import cv2

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
              print('1')

      for (ex,ey,ew,eh) in fist:
          img = cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
          print('2')
     
      for (mx,my,mw,mh) in palm:
          img = cv2.rectangle(img,(mx,my),(mx+mw,my+mh),(0,0,255),2)
          print('3')     
          
      cv2.imshow('img',img) 
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
cap.release()
cv2.destroyAllWindows()