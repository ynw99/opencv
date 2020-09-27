import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def set_gamma(image, gamma=1.0):
    inv_Gamma = 1.0 / gamma
    table = np.array([((i/255.0) ** inv_Gamma) * 255
        for i in np.arange(0, 256)]).astype('uint8')
    return cv.LUT(image, table)

original = cv.imread('D:/Library/Documents/Kuliah/PCV/Datatest/watch.png', 1)
gamma = 0.5
adjusted = set_gamma(original, gamma=gamma)

plt.subplot(121),plt.imshow(cv.cvtColor(original,cv.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv.cvtColor(adjusted,cv.COLOR_BGR2RGB)),plt.title('Gamma Adjusted')
plt.xticks([]),plt.yticks([])
plt.show()