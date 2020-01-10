#Image to array
#created by Asxyzp

import sys
import cv2
import os.path

nameOfFile = input("Name of file for array conversion (w/ file type)? ")
if os.path.isfile(nameOfFile):                          #To check whether the file is in the directory
    Frame = cv2.imread(nameOfFile,cv2.IMREAD_COLOR)     #Reading the photo frame & storing it into an array
    ImgRow = len(Frame)                                 #Stores the number of rows of pixels in the Image
    ImgCol = len(Frame[0])                              #Stores the number of columns of pixels in the Image
    print("Number of rows of Pixel:\t",ImgRow)
    print("Number of cols of Pixel:\t",ImgCol)
    print("Image resolution:\t",ImgRow,"x",ImgCol)

    #Writing Pixel's [R,G,B] array in the Image
    PixR = 0
    ImgArr = open("ImgArr.txt",'w')                     #Opening a file w/ open() & writing text into w/ 'w'   
    while (PixR < ImgRow):
        PixC = 0
        while (PixC < ImgCol):
            ImgArr.write(str(Frame[PixR][PixC]))        #Writing values of individual pixels in the file
            PixC = PixC + 1
        PixR = PixR + 1
    print("\n\nProcess completed.\nImage stored in ImgArr.txt")

else:
    print(nameOfFile+" not found.")
    sys.exit(1)