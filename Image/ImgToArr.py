#Converting Image into array/list & storing it into a text file
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
    print("Number of Pixels:\t",ImgRow*ImgCol)

    #Writing Pixel's [R,G,B] array in the Image
    ImgR = 0
    ImgArrObj = open(nameOfFile+".txt",'a+')            #Opening a file w/ open() & writing text into w/ 'w'
    RowStr = '['                                        #String for storing the entire image's pixel lists as a string
    while ImgR < ImgRow:                                #Traversing through the entire row of the image
        ImgC = 0
        ColStr = '['                                    #String for storing the columns of the image
        while ImgC < ImgCol:                            #Traversing through the entire col of the image
            PixStr = '['+str(Frame[ImgR][ImgC][0])+','+str(Frame[ImgR][ImgC][1])+','+str(Frame[ImgR][ImgC][2])+']'      #Storing pixel's value
            
            if ImgC < ImgCol -1:
                ColStr = ColStr + PixStr + ','          #Adding Pixel + , after an intermediate pixel of a col
            elif ImgC == ImgCol -1:
                ColStr = ColStr + PixStr                #Adding only Pixel, at the last value of the col
            ImgC += 1
        
        if ImgR < ImgRow -1:
            ColStr+='],'                                #Adding ], at the end of col
        elif ImgR == ImgRow -1:
            ColStr+=']'                                 #Adding ] at the end of last col
        
        RowStr += ColStr                                #Adding col to row
        ImgR += 1
    RowStr+=']'                                         #Ending row with ]
    ImgArrObj.write(RowStr)                             #Writing Image array string into a text file
    print("\n\nProcess completed.\nImage stored in ",nameOfFile,".txt")

else:
    print(nameOfFile+" not found.")
    sys.exit(1)
