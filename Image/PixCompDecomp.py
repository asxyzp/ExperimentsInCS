#Program to compose & decompose pixel to integer & integer to pixel, respectively
#Created by asxyzp (Aashish Panigrahi)

import cv2
import numpy

PhotoFrame = []                 #Stores photo frame
PhotoNum   = []                 #Stores integer values after composition of pixel to an integer
NumDecomp  = []                 #Stores decomposed pixel lists             

'''
    Name : PixToInt(Pix)
    Utility : Conversion of a Pixel to an integer
    Parameter(s) : Pix - A numpy array/list which contains pixel [R,G,B] list
    Return value : An integer value after composition 
'''
def PixToInt(Pix):
    return Pix[0]*pow(2,16) + Pix[1]*pow(2,8) + Pix[2]*pow(2,0)     #Composition [REFER: MATH STACKEX]

'''
    Name : IntToPix(Int)
    Utility : Conversion of an integer
    Parameter(s) : Int - An integer for pixel decomposition
    Return value : A list/numpy array containing pixel images
'''
def IntToPix(Int):
    R = Int//pow(2,16)                                             #R Decomposition
    Int = Int - R*pow(2,16)
    G = Int//pow(2,8)                                              #G Decomposition
    B = Int - G*pow(2,8)                                           #B Decomposition
    return list([R,G,B])

'''
    Name : RowPixToInt(ImgRow)
    Utility : Converting a row of [R,G,B] pixels into a row of integers by composition
    Parameter : ImgRow : A Row of pixels of an image
    Return value : None
'''
def RowPixToInt(ImgRow):
    Row = []
    for pixel in ImgRow:
        Int = PixToInt(pixel)   #Converts Pixels into Integers
        Row.append(Int)
    PhotoNum.append(list(Row))

'''
    Name : RowIntToPix(NumRow)
    Utility : Converting a row of integers into a row of Pixels by decomposition
    Parameter : NumRow : A row of integers for decomposition
    Return value : None
'''
def RowIntToPix(NumRow):
    Row = []
    for num in NumRow:         #Converts Numbers into Pixels
        Pix = IntToPix(num)
        Row.append(list(Pix))
    NumDecomp.append(list(Row))

'''
    Name : ImgArr(FileName)
    Utility : Converting an image into a list
    Parameter : FileName : Name of file of the image
    Return value : None
'''
def ImgArr(FileName):
    PhotoFrame = cv2.imread(FileName,cv2.IMREAD_COLOR)
    for PixRow in PhotoFrame:
        RowPixToInt(PixRow)

'''
    Name : ArrImg(ArrName)
    Utility : Converting an array into an image
    Parameter : ArrName : Name of the list/numpy array storing the photo frame
    Return value : None
'''
def ArrImg(ArrName):
    for NumRow in ArrName:
        RowIntToPix(NumRow)
    cv2.imwrite("DEC"+FileName,numpy.asarray(NumDecomp))

FileName = input("Name of image file/path (w/ file type. e.g. PNG/JPEG)?\t")
ImgArr(FileName)
ArrImg(PhotoNum)