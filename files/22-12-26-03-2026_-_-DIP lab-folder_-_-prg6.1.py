import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Ed.png')
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)
sobel_mag = np.uint8(sobel_mag)

# Canny
canny_edges = cv2.Canny(gray, 100, 200)

# Plot
fig, axs = plt.subplots(1, 3, figsize=(10, 4))

axs[0].imshow(image_rgb)
axs[0].set_title('Original')

axs[1].imshow(sobel_mag, cmap='gray')
axs[1].set_title('Sobel')

axs[2].imshow(canny_edges, cmap='gray')
axs[2].set_title('Canny')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
