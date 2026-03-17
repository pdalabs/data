import cv2
import matplotlib.pyplot as plt
image=cv2.imread('c4.jpg')
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
center=(image_rgb.shape[1]//2,image_rgb.shape[0]//2)
angle=30
scale=1
Rotation_matrix=cv2.getRotationMatrix2D(center,angle,scale)
Rotated_image=cv2.warpAffine(image_rgb,Rotation_matrix,(image.shape[1],image.shape[0]))
fig,axs=plt.subplots(1,2,figsize=(7,4))
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(Rotated_image)
axs[1].set_title('Rotated Image')
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])
plt.tight_layout()
plt.show()


