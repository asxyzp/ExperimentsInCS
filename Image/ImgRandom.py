#Generating a pseudo-random Image : An Image where each Pixel's [R,G,B] value is selected randomly between 0-255
#Created by Aashish Loknath Panigrahi

import sys
import cv2
import random
import numpy

'''
    Function: GenerateRandomPixel()
    Functionality: Will generate a random pixel
    Parameter(s): NILL
    Output: [R,G,B] list where R,G,B are random values between 0-255
'''
def GenerateRandomPixel():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    return list([R,G,B])        #Returns a pixel's [R,G,B] list

'''
    Function: GenerateCol()
    Functionality: Will generate a list storing y pixel values for an image with x*y resolution
    Parameter(s): ColSize - Will store the column size
    Output: [[R1,G1,B1], ..... , [Ry,Gy,By]] where Ri,Gi,Bi are random values between 0-255
'''
def GenerateCol(ColSize):
    tempCol=[]
    for i in range(ColSize):
        tempCol.append(GenerateRandomPixel())
    return list(tempCol)        #Returns a column list of pixel values for an image with x*y res.

'''
    Function: GenerateRow()
    Functionality: Will generate a list storing x columns (w/ y pixels) for an image with x*y resolution
    Parameters(x) : ColSize - Will store the column size
                    RowSize - Will store the row size
    Output :
    [
        [[R11,G11,B11],...,[R1y,G1y,B1y]],
        .
        .
        [[Rx1,Gx1,Bx1],...,[Rxy,Gxy,Bxy]],
    ] where Ri,Gi,Bi will be random values between 0-255
'''
def GenerateRow(ColSize,RowSize):
    tempRow=[]
    for i in range(RowSize):
        tempRow.append(GenerateCol(ColSize))
    return list(tempRow)    #Returns a list which stores an image of x*y res.

'''
    Function: GenerateRandomImage(NameOfFile)
    Functionality: Will generate a random image & will store it in NameOfFile.FileType
    Parameter(s): NameOfFile (w/o file type)
'''
def GenerateRandomImage():
    NameOfFile = input("Name of file in which random image will be stored (w/o file type)?\t")
    ColSize = int(input("Column size of an image?\t"))
    RowSize = int(input("Row size of an image?   \t"))
    NameOfFile += ".png"
    cv2.imwrite(NameOfFile,numpy.asarray(GenerateRow(ColSize,RowSize)))
    #numpy.asarray(listName) converted the image list into a numpy array for writing into an image using cv2.imwrite()


RandomIngNum = int(input("Number of random images to be generated?\t"))
i = 0
while i<RandomIngNum:
    GenerateRandomImage()
    i+=1