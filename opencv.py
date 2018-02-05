import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

import cv2

for i in enumerate({'r', 'b', 'g'}):
    print(type(i), i)


def grayscaleimage():
    img = cv2.imread('loof.jpg', cv2.IMREAD_GRAYSCALE)
    # IMREAD_GRAYSCALE 0
    #IMREAD_COLOR -1
    #IMREAD_UNCHANGED =-1
    # OR
    print(img.shape)
    print(img.shape[0], img.shape[1])
    print(img[0, 0])  # pixel value
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# a HSV image hue - saturation - value


def HSVimage():  # playing with HSV
    img1 = cv2.imread('loof.jpg')
    img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV image or normal image', img)
    cv2.imshow('Hue channel', img[:, :, 0])
    cv2.imshow('Saturation channel', img[:, :, 1])
    cv2.imshow('Value channel', img[:, :, 2])
    cv2.imshow('HSV image or normal image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# R G B COLOR


def BGRimager():
    img = cv2.imread('msnp.jpg')
    cv2.imshow('Image', img)
    B, G, R = cv2.split(img)
    zeros = np.zeros(img.shape[:2], dtype="uint8")
    print(zeros[0])
    cv2.imshow('R', cv2.merge([zeros, zeros, R]))
    cv2.imshow('G', cv2.merge([zeros, G, zeros]))
    cv2.imshow('B', cv2.merge([B, zeros, zeros]))

    cv2.imwrite('R.jpg', cv2.merge([zeros, zeros, R]))
    cv2.imwrite('G.jpg', cv2.merge([zeros, G, zeros]))
    cv2.imwrite('B.jpg', cv2.merge([B, zeros, zeros]))

    # cv2.imshow('B',B)
    # cv2.imshow('G',G)
    # cv2.imshow('R',R)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def HISTImage():
    img = cv2.imread('loof.jpg')
    histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

    color = {'b', 'g', 'r'}

    for i, col in enumerate(color):
        hist2 = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist2, color=col)
        plt.xlim([0, 256])

    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def shapes():
    image = np.zeros((786, 1024, 3), np.uint8)
    # shows a black image with shapes
    #def line(img, start position, End position, color(r,g,b), thickness=None, lineType=None, shift=None)
    cv2.line(image,(0,500),(511,500),(12,145,85),60)

    #def rectangle(img, diagonal 1, diagonal 2, color(r,b,g), thickness=None, lineType=None, shift=None)
    cv2.rectangle(image,(100,100),(300,250),(0,0,255),-1)

    #def circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
    cv2.circle(image,(350,350),100,(204, 122, 0),-1)

    #polylines
    points=np.array([[10,50],[400,50],[90,200],[50,500]],np.int32)
    points=points.reshape(-1,1,2)
    cv2.polylines(image,[points],True,(0,0,255),3)
    


    # text in image
    cv2.putText(image,'Hello Lince',(75,200),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0),3)
    cv2.imshow("Hello Lince!",image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()














def optioner(option):
    optdict = {1: grayscaleimage, 2: HSVimage, 3: BGRimager, 4: HISTImage, 5: shapes,}

    return optdict[option]()


option = int(input(" \
#1 grayscaleimage() \n \
#2 HSVimage() \n \
#3 BGRimager()\n \
#4 HISTImage()\n \
#5 Shapes()\n \
\n \
Enter option"))

optioner(option)


# grayscaleimage()
# HSVimage()
# BGRimager()
# HISTImage()
