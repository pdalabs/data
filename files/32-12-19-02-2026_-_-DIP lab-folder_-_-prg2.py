import cv2
import numpy as np
img1= cv2.imread('Input1.jpg')
img2= cv2.imread('Input2.jpg')

height,width=img1.shape[:2]
img2=cv2.resize(img2,(width,height))

cv2.imshow('Image1',img1)
cv2.imshow('Image2',img2)

dest_and=cv2.bitwise_and(img2,img1,mask=None)
cv2.imshow('Bitwise_AND',dest_and)

dest_or=cv2.bitwise_or(img2,img1,mask=None)
cv2.imshow('Bitwise_OR',dest_or)

dest_xor=cv2.bitwise_xor(img2,img1,mask=None)
cv2.imshow('Bitwise_XOR',dest_xor)

dest_not=cv2.bitwise_not(img1,mask=None)
cv2.imshow('Bitwise_NOT',dest_not)
