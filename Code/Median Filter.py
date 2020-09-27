import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

pic = cv.imread("D:/Library/Documents/Kuliah/PCV/Datatest/108073.png")
median = cv.medianBlur(pic,3)

plt.subplot(121),plt.imshow(cv.cvtColor(pic,cv.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv.cvtColor(median,cv.COLOR_BGR2RGB)),plt.title('Median Blur')
plt.xticks([]),plt.yticks([])
plt.show()