import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Ed.png')
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ---------------- Sobel ----------------
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)
sobel_mag = np.uint8(sobel_mag)

# ---------------- Canny ----------------
canny_edges = cv2.Canny(gray, 100, 200)

# ---------------- Laplacian ----------------
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# ---------------- Prewitt ----------------
kernelx = np.array([[1, 0, -1],
                    [1, 0, -1],
                    [1, 0, -1]])

kernely = np.array([[1, 1, 1],
                    [0, 0, 0],
                    [-1, -1, -1]])

prewitt_x = cv2.filter2D(gray, -1, kernelx)
prewitt_y = cv2.filter2D(gray, -1, kernely)
prewitt = np.sqrt(prewitt_x**2 + prewitt_y**2)
prewitt = np.uint8(prewitt)

# ---------------- Plot ----------------
fig, axs = plt.subplots(1, 5, figsize=(15, 4))

axs[0].imshow(image_rgb)
axs[0].set_title('Original')

axs[1].imshow(sobel_mag, cmap='gray')
axs[1].set_title('Sobel')

axs[2].imshow(canny_edges, cmap='gray')
axs[2].set_title('Canny')

axs[3].imshow(laplacian, cmap='gray')
axs[3].set_title('Laplacian')

axs[4].imshow(prewitt, cmap='gray')
axs[4].set_title('Prewitt')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
