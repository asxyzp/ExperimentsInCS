#Program to capture an image & store it in a File
#Created by Asxyzp
import cv2

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
else:
  print("The Frame has not been captured correctly")
