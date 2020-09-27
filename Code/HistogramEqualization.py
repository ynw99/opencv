import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

pic = cv.imread("D:/Library/Documents/Kuliah/PCV/Datatest/he.jpg",0)
equ = cv.equalizeHist(pic)

fig = plt.figure(1)
plt.subplot(221),plt.imshow(cv.cvtColor(pic,cv.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(cv.cvtColor(equ,cv.COLOR_BGR2RGB)),plt.title('Equalized')
plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.hist(pic.flatten(),256,[0,256], color = 'r'),plt.title('Histogram Awal')
plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.hist(equ.flatten(),256,[0,256], color = 'r'),plt.title('Histogram Akhir')
plt.xticks([]),plt.yticks([])

plt.show()