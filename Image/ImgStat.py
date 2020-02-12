#Plotting frequency of pixel color in a given image
#Created by asxyzp (Aashish Panigrahi)

import matplotlib.pyplot as plt
import cv2
import numpy

RGBArr = []                     #Will Store RGB pixel list for conversion into hex value
RGBHex = []                     #Will Store RGB hex values for plotting
PixFrq =[]                      #Will store frequency for each pixel
tempArr = []                    #Temporary array for storing pixel values in a 1-D list 

'''
    Name : RGBToHex(RGBList)
    Utility : Conversion of list [R,G,B] into a hexadecimal value
    Parameter(s) : RGBList - A list storing pixel values [R,G,B]
    Return value : Hex - Hexadecimal value corresponding to [R,G,B] pixel
'''
def RGBToHex(RGBList):
    R = hex(RGBList[0])
    G = hex(RGBList[1])
    B = hex(RGBList[2])
    return R+G[2:4]+B[2:4]
'''
    Name : RGBArrToRGBHex()
    Utility : Convets & stores values of RGBArr to RGBHex
    Parameter(s) : None
    Return value : None
'''
def RGBArrToRGBHex():
    for i in range(len(RGBArr)):
        RGBHex.append(RGBToHex(RGBArr[i]))

'''
    Name : FreqPlot()
    Utility : Generates frquency plot for each pixel
    Parameters(s) : None
    Return value : None
'''
def FreqPlot():
    countArr = []
    for i in range(len(RGBHex)):
        countArr.append(i)
    '''
    #Plotting points
    plt.plot(countArr,PixFrq,'k.')
    plt.xlabel("Pixel values")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()
    '''
    #Plotting bar graph
    plt.bar(countArr,PixFrq)
    plt.xlabel("Pixel values")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()

'''
    Name : PixFreq(ImgFile)
    Utility : Computes the frequency of [R,G,B] lists from an image & stores it in PixFreq
    Parameter(s) : ImgFile - Name of the image file for which stats have to be formed
    Return value : None
'''
def PixFreq(ImgFile):
    ImgFrame = cv2.imread(ImgFile,cv2.IMREAD_COLOR)     #Reading Image
    ImgRowLen = len(ImgFrame)                           #Stores the length of row of pixels
    ImgColLen = len(ImgFrame[0])                        #Stores the length of col of pixels
    
    #For storing pixel values in tempArr
    #2D list to 1D list conversion of pixels
    for i in range(ImgRowLen):                          
        for j in range(ImgColLen):
            tempArr.append(numpy.ndarray.tolist(ImgFrame[i][j]))
            #numpy.ndarray.tolist() converts numpy array to list
    
    for i in range(len(tempArr)):
        if tempArr[i] not in RGBArr:                    #Stores the value of unique value in the list  
            RGBArr.append(tempArr[i])                   
    
    #Stores freq. of each pixel
    for i in range(len(RGBArr)):
        count = 0
        for j in range(len(tempArr)):
            if RGBArr[i] == tempArr[j]:
                count+=1
        PixFrq.append(count)
    
    RGBArrToRGBHex()                                   #Conversion of [R,G,B] to hex
    FreqPlot()                                         #Frequency plot

ImgName =  input("Name of image file/path (w/ file type. e.g. PNG/JPEG)?\t")
PixFreq(ImgName)