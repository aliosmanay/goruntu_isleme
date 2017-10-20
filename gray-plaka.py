
# coding: utf-8

# In[1]:

ls


# In[2]:

import matplotlib.pyplot as plt
import numpy as np
img_1=plt.imread("test_1.jpg")
img_1.ndim
img_1.shape
img_2=img_1[1:1080:2,1:1920:2]
img_2.ndim,img_2.shape
plt.imshow(img_2)
plt.show()
img_2


# In[4]:

plt.imshow(img_1,plt.cm.gray)
plt.show()


# In[6]:

img_3=np.zeros((img_2.shape[0:2]))
img_3.shape
img_4=np.zeros((img_2.shape[0:2]))
img_4.shape
img_5=np.zeros((img_1.shape[0:2]))
img_2=img_1
img_2.shape,img_5.shape
threshold=100
for i in range(img_2.shape[0]):
    for j in range(img_2.shape[1]):
        n=img_2[i,j,0]/3 + img_2[i,j,1]/3 + img_2[i,j,2]/3
        img_3[i,j]=n
        if n > threshold:
            img_4[i,j] =255
        else:
            img_4[i,j]=0
plt.subplot(1,3,1),plt.imshow(img_2)
plt.subplot(1,3,2),plt.imshow(img_4, plt.cm.binary)
plt.show()
        


# In[7]:

plt.imshow(img_3,plt.cm.gray)
plt.show()


# In[8]:

plt.imshow(img_4, plt.cm.binary)
plt.show()


# In[9]:

img_1=plt.imread("plaka.jpg")
img_1.ndim,img_1.shape
img_5=np.zeros((img_1.shape[0:2]))
img_2=img_1
img_2.shape,img_5.shape
threshold=100
for i in range(img_2.shape[0]):
    for j in range(img_2.shape[1]):
        n=img_2[i,j,0]/3 + img_2[i,j,1]/3 + img_2[i,j,2]/3
        img_3[i,j]=n
        if n > threshold:
            img_5[i,j] =255
        else:
            img_5[i,j]=0
plt.subplot(1,3,1),plt.imshow(img_2)
plt.subplot(1,3,2),plt.imshow(img_5, plt.cm.binary)
plt.show()
        


# In[ ]:



