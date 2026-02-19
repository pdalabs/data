import cv2
img=cv2.imread("image1.png")

h= img.shape[0]
w= img.shape[1]
pixels=h*w

print("Height=",h)
print("Width=",w)

print("Tota Number of pixels=",pixels,"pixels")
