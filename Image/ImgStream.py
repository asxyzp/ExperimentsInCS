#Capturing a sequence of images using OpenCV
#Created by Asxyzp

import os
import cv2
import sys

NameOfPhotoStream = input("Name of photo stream? ")

#Creating a directory to store the photo stream
try:
    os.mkdir(NameOfPhotoStream)                             #To create directory
    print(NameOfPhotoStream," stream directory created")
except FileExistsError:                                     #If directory already exists
    print(NameOfPhotoStream," stream directory already exists")
    sys.exit(1)                                             #Exiting the program with exit_code=1 representing unsuccesful termination

NumberOfPhotos = int(input("Number of photos in the photo stream? "))
i = 0                                                       #For iteration
while (i<NumberOfPhotos):
    PhotoObj = cv2.VideoCapture(0)                          #Capturing photo stream using VideoCapture() class
                                                            #0 specifies that device's integrated camera is used to capture photo stream
    PhotoTuple = PhotoObj.read()
    if PhotoTuple[0]:
        Frame = PhotoTuple[1]
        PathName = NameOfPhotoStream+"/"+NameOfPhotoStream+str(i)+".jpeg"
        cv2.imwrite(PathName,Frame)                         #Will write image into the directory
        PhotoObj.release()                                  #Will release the camera
        print("Photo frame ",i+1," generated.")
    else:
        print("Photo frame not captured correctly")
        PhotoObj.release()
        break
    i += 1

