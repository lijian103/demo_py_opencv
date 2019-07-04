import numpy as np
import cv2
import matplotlib.pyplot as plt
import scipy
import skimage

x_axis = np.linspace(0, np.pi*20,1080)#np.arange(0, 1080, 1, dtype="uint8")
y_axis1 = 90 * np.sin(x_axis) + 120
plt.plot(x_axis, np.uint8(y_axis1))
plt.show()