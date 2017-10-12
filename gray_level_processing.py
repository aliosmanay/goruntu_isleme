
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


# In[2]:

ls


# In[3]:

import matplotlib.pyplot as plt
import numpy as np
img_1=plt.imread("a1.jpg")


# In[4]:

img_1.ndim,img_1.shape


# In[5]:

plt.imshow(img_1)
plt.show()


# In[6]:

def convertRGBPixelToGrayLevel(RGB_Pixel):
    return RGB_Pixel[0]/3 + RGB_Pixel[1]/3 + RGB_Pixel[2]/3


# In[7]:

convertRGBPixelToGrayLevel([2,8,9])


# In[11]:

img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
img_2.shape


# In[13]:

for i in range (img_1.shape[0]):
    for j in range (img_1.shape[1]):
        img_2[i,j]=convertRGBPixelToGrayLevel(img_1[i,j,:])


# In[18]:

plt.subplot(1,2,1)
plt.imshow(img_1)
plt.subplot(1,2,2)
plt.imshow(img_2, cmap='gray')
plt.show()


# In[20]:

import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave
def convertRGB_to_GrayLevel(image_1):
    img_1=plt.imread(image_1)
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range(img_1.shape[0]):
        for j in range(img_1.shape[1]):
            img_2[i,j]=img_1[i,j,0]/3 + img_1[i,j,1]/3 + img_1[i,j,2]/3
    imsave(image_1 + "gray.jpg", img_2)
    plt.subplot(1,2,1)
    plt.imshow(img_1)
    plt.subplot(1,2,2)
    plt.imshow(img_2, cmap='gray')
    plt.show()
convertRGB_to_GrayLevel("test_10.jpg")


# In[ ]:



