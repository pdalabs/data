import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread('c4.jpg')
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
width=image_rgb.shape[1]
height=image_rgb.shape[0]
tx=-30
ty=-50
translation_matrix=np.array([[1,0,tx],[0,1,ty]],dtype=float)
translated_image=cv2.warpAffine(image_rgb,translation_matrix,(width,height))
fig,axs=plt.subplots(1,2,figsize=(7,4))
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(translated_image)
axs[1].set_title('Translated Image')
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])
plt.tight_layout()
plt.show()


