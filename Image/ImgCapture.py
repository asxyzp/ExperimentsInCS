#Program to capture an image & store it in a File
#Created by Asxyzp

import cv2
import time

#time.sleep(t) allows to freez a thread
noOfSec = 0
while noOfSec<=1:
  noOfSec = int(input("Seconds to take photo stream after?\t"))
  if noOfSec<=1:
    print("Enter a number greater than 1\n")              

for i in range(1,noOfSec):                            
  print("PhotoStream to be taken in ",i," second(s).")    #Self-timer before image is taken
  time.sleep(1)                                           #Will delay the execution by 1sec.

#VideoCapture class allows capturing of video from image sequences, videos or camera
#cv2.VideoCapture(index) returns an object
#index parameter of VideoCapture() allows to choose from primary/secondary camera
PhotoObj = cv2.VideoCapture(0)

#PhotoObj.read() will return a tuple w/ 2 values
#The 1st value of the tuple will be a boolean which will store whether the frame has been captured correcctly.
#The 2nd value of the tuple will be a numpy arrray which will store the frame.
PhotoTuple = PhotoObj.read()
if PhotoTuple[0]:
  Frame = PhotoTuple[1]                 #Stores Image in a numpy array
  nameOfFile = input("Name of file? ")  #Accepts the name of the file in which image will be stored
  nameOfFile = nameOfFile + ".jpeg"     #Adding format in which the name will be stored
  cv2.imwrite(nameOfFile,Frame)         #For writing an image at a particular location
  PhotoObj.release()
else:
  print("The Frame has not been captured correctly")
  PhotoObj.release()
