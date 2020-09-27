import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

pic = cv.imread("D:/Library/Documents/Kuliah/PCV/Datatest/boy.bmp")
blur = cv.blur(pic,(7,7))

plt.subplot(121),plt.imshow(cv.cvtColor(pic,cv.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv.cvtColor(blur,cv.COLOR_BGR2RGB)),plt.title('Average Blur')
plt.xticks([]),plt.yticks([])
plt.show()
