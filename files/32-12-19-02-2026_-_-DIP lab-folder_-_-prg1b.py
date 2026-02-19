import cv2
import numpy as np
image1=cv2.imread('image1.png')

image2= cv2.imread('image2.png')

cv2.imshow('Image1',image1)
cv2.imshow('Image2',image2)


# Get height and width from image1
h, w = image1.shape[:2]

# Resize image2 to match image1
image2 = cv2.resize(image2, (w, h))

#image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

ImgSum=cv2.add(image1,image2)
cv2.imshow('image3',ImgSum)

subtracted=cv2.subtract(image1,image2)
cv2.imshow('image4',subtracted)
