
# coding: utf-8

# In[3]:

import matplotlib.pyplot as plt
import numpy as np
def def_mask():
        mask_1=[[1,1,1],[1,1,1],[1,1,1]]
        mask_1,mask_1[0][0],mask_1[1][1],mask_1[2][2]
        for i in range(3):
            for j in range(3):
                print(mask_1[i][j],end=" ")
            print()
        return mask_1

def my_dilation(img_1,mask):
    m=img_1.shape[0]
    n=img_1.shape[1]
    img_2=np.random.randint(0,1,(m,n))
    for i in range(1,m-1):
         for j in range(1,n-1):
            x_1=img_1[i-1,j-1] and mask[0][0]
            x_2=img_1[i-1,j] and mask[0][1]
            x_3=img_1[i-1,j+1] and mask[0][2]
            x_4=img_1[i,j-1] and mask[1][0]
            x_5=img_1[i,j] and mask[1][1]
            x_6=img_1[i,j-1] and mask[1][2]
            x_7=img_1[i+1,j-1] and mask[2][0]
            x_8=img_1[i+1,j] and mask[2][1]
            x_9=img_1[i+1,j+1] and mask[2][2]
            result_1=x_1 or x_2 or x_3 or x_4 or x_5
            result_2=x_6 or x_7 or x_8 or x_9
            result = result_1 or result_2
            img_2[i,j]=result
    return img_2     


# In[4]:

img=plt.imread("ali.jpg")
black_white=np.zeros(img.shape[0:2])
thresold=100

for i in range(black_white.shape[0]):
    for j in range(black_white.shape[1]):
        a=img[i,j,0]/3+img[i,j,1]/3+img[i,j,2]/3
        if a>thresold:
            black_white[i,j]=0
        else:
            black_white[i,j]=255
img_3=my_dilation(black_white,def_mask())
plt.subplot(1,2,1),plt.imshow(black_white,plt.cm.binary)
plt.subplot(1,2,2),plt.imshow(img_3,plt.cm.binary)
plt.show()


# In[ ]:



