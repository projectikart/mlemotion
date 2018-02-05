import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
import cv2
import os


def Transalations():
    image = cv2.imread("test.jpg")
    height, width = image.shape[:2]
    qheight, qwidth = height / 4, width / 4
    T = np.float32([[1, 0, qwidth], [0, 1, qheight]])
    img = cv2.warpAffine(image, T, (width * 2, height * 2))
    cv2.imshow('Transalations', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
    

def Rotation():
    image = cv2.imread("test.jpg")
    height, width = image.shape[:2]
    #def getRotationMatrix2D(center, angle, scale)
    rotation_matrix=cv2.getRotationMatrix2D((width*2,0),45,1)
    rotated_image=cv2.warpAffine(image,rotation_matrix,(width*3,height*3))
    
    cv2.imshow("rotated and scaled image",rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image = cv2.imread("test.jpg")
    img=cv2.transpose(image)
    cv2.imshow("",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pyramid():
    image = cv2.imread("test.jpg")
    small=cv2.pyrDown(image)
    large=cv2.pyrUp(image)

    cv2.imshow("small",small)
    cv2.imshow("large",large)
    cv2.imshow("large",cv2.pyrUp(large))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cropping():
    image = cv2.imread("loof.jpg")
    h,w=image.shape[:2]

    startrow,startcol=int(h*.25),int(w*.25)
    endrow, endcol=int(h*.75),int(w*.75)

    cropped=image[startrow:endrow,startcol:endcol]

    cv2.imshow("cropped image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def blurring():
    image = cv2.imread("loof.jpg")

    blur=cv2.blur(image,(3,3))
    cv2.imshow("Averaging",blur)
    

    Gaussian=cv2.GaussianBlur(image,(7,7),0)
    cv2.imshow('Gaussian Blurring',Gaussian)
    

    median=cv2.medianBlur(image,5)
    cv2.imshow('Median Blurring',median)
    

    bilateral =cv2.bilateralFilter(image,9,75,75)
    cv2.imshow('Bilateral Blurring',bilateral)
    cv2.waitKey(0)

    cv2.destroyAllWindows()





#Transalations()
#Rotation()
#pyramid()
#cropping()
blurring()
#


