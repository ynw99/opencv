import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

pic = cv.imread("D:/Library/Documents/Kuliah/PCV/Datatest/airplane.png")
negatif = cv.bitwise_not(pic)

plt.subplot(121),plt.imshow(cv.cvtColor(pic,cv.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv.cvtColor(negatif,cv.COLOR_BGR2RGB)),plt.title('Negative Image')
plt.xticks([]),plt.yticks([])
plt.show()