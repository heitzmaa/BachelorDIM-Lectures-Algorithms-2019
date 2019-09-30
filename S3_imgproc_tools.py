# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:22:50 2019

@author: heitzmaa
"""

import cv2
import numpy as np

img_gray=cv2.imread("imageToInvert.jpg",0)
img_bgr=cv2.imread("imageToInvert.jpg",1)

print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))

cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr) 
cv2.waitKey()

"""
Inverse les couleurs de la photo mais pas manuellement
img = cv2.imread("imageToInvert.jpg")
cv2.imshow("Pic",img)
 
img_not = cv2.bitwise_not(img)
cv2.imshow("Invert1",img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
def invert_colors_manual(input_img : ndarray):
    
    