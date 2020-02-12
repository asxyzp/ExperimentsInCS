#Description: Converting RGB image to Greyscale/Grayscale image
#Author(s)  : asxyzp

import cv2
import sys
import os.path

'''
    Name : RGBToGrey(FileName)
    Utility : RGB to Greyscale converter program
    Parameter(s) : FileName is the name of the image file for which the conversion has to be done
    Return value : None
'''
def RGBToGrey(FileName):
    if os.path.isfile(FileName):                            #Checking whether the image exists or not
        Frame = cv2.imread(FileName,cv2.IMREAD_COLOR)       #Stores image into a photo frame
        RowSize = len(Frame)                                
        ColSize = len(Frame[0])
        for i in range(RowSize):
            for j in range(ColSize):
                Grey = 0.3*Frame[i][j][0] + 0.59*Frame[i][j][1] + 0.11*Frame[i][j][2] #Formula for RGB to Greyscale conversion
                Frame[i][j][0] = Grey
                Frame[i][j][1] = Grey
                Frame[i][j][2] = Grey
        FileName="Grey_"+FileName
        cv2.imwrite(FileName,Frame)
    else:
        print("Image file doesn't exists.\nEnter proper file name.")
        sys.exit(1)

FileName = input("Name of image file for greyscale conversion (w/ file type)?\t")
RGBToGrey(FileName)