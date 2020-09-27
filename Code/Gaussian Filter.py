import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

pic = cv.imread("D:/Library/Documents/Kuliah/PCV/Datatest/fruits.png")
gaussian = cv.blur(pic,(7,7),0)

plt.subplot(121),plt.imshow(cv.cvtColor(pic,cv.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv.cvtColor(gaussian,cv.COLOR_BGR2RGB)),plt.title('Gaussian Blur')
plt.xticks([]),plt.yticks([])
plt.show()