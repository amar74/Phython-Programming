import cv2
import numpy as np
import matplotlib.pyplot as mpl
#start load an image
imLoad = cv2.imread("test.jpg")
cv2.imshow("Window Name", imLoad)
cv2.waitKey(0)
cv2.destroyAllWindows()