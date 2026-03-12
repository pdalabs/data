import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('Inputp5.jpg')

image_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

width=image_rgb.shape[1]
height=image_rgb.shape[0]

tx=60
ty=90
translation_matrix=np.array([[1,0,-tx],[0,1,ty]],dtype=np.float32)
translation_matrix=np.array([[1,0,tx],[0,1,-ty]],dtype=np.float32)
translation_matrix=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32)

translation_matrix=np.array([[1,0,-tx],[0,1,-ty]],dtype=np.float32)

translated_image=cv2.warpAffine(image_rgb,translation_matrix,(width,height))

fig,axs=plt.subplots(3,2,figsize=(10,10))

axs[0,0].imshow(image_rgb)
axs[0,0].set_title('Original Image')

axs[1,0].imshow(translated_image)
axs[1,0].set_title('Image Transformation 1')

axs[1,1].imshow(translated_image)
axs[1,1].set_title('Image Transformation 2')

axs[2,0].imshow(translated_image)
axs[2,0].set_title('Image Transformation 3 ')

axs[2,1].imshow(translated_image)
axs[2,1].set_title('Image Transformation 4')


for ax in axs.ravel():
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()








    
