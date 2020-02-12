#Description: Converting greyscale image to binary image
#Author(s)  : asxyzp

import os.path
import sys
import cv2

'''
    Name : GreyToBinary(FileName)
    Utility : Converts GreyScale image to Binary image
    Parameter(s) : FileName, which is the name of the image file
    Return value : None 
'''
def GreyToBinary(FileName):
    if os.path.isfile(FileName):                            #Checking whether the image exists or not
        Frame = cv2.imread(FileName,cv2.IMREAD_COLOR)       #Stores image into a photo frame
        RowSize = len(Frame)                                
        ColSize = len(Frame[0])
        for i in range(RowSize):
            for j in range(ColSize):
                if (Frame[i][j][0]<127):                    #Converting all pixels w/ intensity below 127 to Black
                    Frame[i][j][0] = 0
                    Frame[i][j][1] = 0
                    Frame[i][j][2] = 0
                elif (Frame[i][j][0]>127):                  #Converting all pixels w/ intensity above 127 to Black
                    Frame[i][j][0] = 255
                    Frame[i][j][1] = 255
                    Frame[i][j][2] = 255
        FileName="Bin_"+FileName
        cv2.imwrite(FileName,Frame)
    else:
        print("Image file doesn't exists.\nEnter proper file name.")
        sys.exit(1)

FileName = input("Name of image file for greyscale conversion (w/ file type)?\t")
GreyToBinary(FileName)