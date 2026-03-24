import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread('aq.jpg')
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
edges=cv2.Canny(image=image_rgb,threshold1=150,threshold2=100)
fig,axs=plt.subplots(1,2,figsize=(7,4))
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(edges)
axs[1].set_title('Image Edges')
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])
plt.tight_layout()
plt.show()


