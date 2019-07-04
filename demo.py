import sys
import constant
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from my_lib import MyFile
import cv2
import matplotlib.pyplot as plt
if __name__ == "__main__":
    img = cv2.imread('./1.JPg')
    img_gray = cv2.imread('./1.JPg', cv2.IMREAD_GRAYSCALE)
    dimensions = img.shape
    print(dimensions)
    total_number_of_elements = img.size
    print(total_number_of_elements)
    image_dtype = img.dtype
    print(image_dtype)
    img_OpenCV = cv2.imread('./1.JPg')
    b, g, r = cv2.split(img_OpenCV)
    img_matplotlib = cv2.merge([r, g, b])

    #plt.show
    plt.subplot(1,2,1)
    plt.imshow(img_OpenCV)
    plt.subplot(1,2,2)
    plt.imshow(img_matplotlib)
    # plt.show()
    print("red: {}".format(constant.RED))

