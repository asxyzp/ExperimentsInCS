#Description: Generating a pseudorandom image with prime numbers
#Author(s)  : asxyzp

import cv2
import random
import numpy

PrimeArr = []                       #Will store prime numbers between 0-255

'''
    Name : CheckPrime(num)
    Utility : Checks whether the number num is prime
    Parameter(s) : num (a positive integer)
    return value : boolean (true : If num is prime, false : If num is not prime)
'''
def CheckPrime(num):
    if num<2:                       #0,1 aren't prime
        #print(num," is not prime\n")
        return False
    elif num==2:                    #2 is prime
        #print(num," is not prime\n")
        return True
    elif num>2:
        for i in range(2,num):
            if num%i==0:            #If num>2 & num is divisible by any number between 2 & num-1, then num isn't prime
                return False
        return True    

'''
    Name : GeneratePrimeArr()
    Utility : Generates & stores prime numbers between 0 & 255 in primeArr
    Parameter(s) : None
    Return value : None
'''
def GeneratePrimeArr():
    for i in range(0,256):
        if CheckPrime(i):           #Appends number if prime
            PrimeArr.append(i)

GeneratePrimeArr()                  #Generates an array of prime numbers

'''
    Function: GenerateRandomPixel()
    Functionality: Will generate a random pixel from PrimeArr list
    Parameter(s): NILL
    Output: [R,G,B] list where R,G,B are random prime values between 0-255
'''
def GenerateRandomPixel():
    R = random.choice(PrimeArr) #random.choice(PrimeArr) chooses random values from PrimeArr list
    G = random.choice(PrimeArr)
    B = random.choice(PrimeArr)
    return list([R,G,B])        #Returns a pixel's [R,G,B] list

'''
    Function: GenerateCol()
    Functionality: Will generate a list storing y pixel values for an image with x*y resolution
    Parameter(s): ColSize - Will store the column size
    Output: [[R1,G1,B1], ..... , [Ry,Gy,By]] where Ri,Gi,Bi are random prime values between 0-255
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
    ] where Ri,Gi,Bi will be random prime values between 0-255
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
def GenerateRandomImage(NameOfFile,ColSize,RowSize):
    NameOfFile += ".png"
    cv2.imwrite(NameOfFile,numpy.asarray(GenerateRow(ColSize,RowSize)))
    #numpy.asarray(listName) converted the image list into a numpy array for writing into an image using cv2.imwrite()


RandomIngNum = int(input("Number of random images to be generated?\t"))
i = 0
NameOfFile = input("Name of file in which random image will be stored (w/o file type)?\t")
ColSize = int(input("Column size of an image?\t"))
RowSize = int(input("Row size of an image?   \t"))
while i<RandomIngNum:
    GenerateRandomImage(NameOfFile+str(i+1),ColSize,RowSize)
    i+=1
print("Random prime images generated :)")