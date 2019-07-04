import numpy as np
import constant
import cv2 as cv
import matplotlib.pyplot as plt
image = np.zeros((500,400, 3), dtype="uint8")
image[:] = constant.LIGHT_GRAY
cv.imshow("image",image)

#show_in_matplot
image_matplotlib = image[:, :, ::-1]
# cv.line(image, (50, 60), (300,60),constant.GREEN , 8)
# cv.rectangle(image, (10, 50), (60, 300), constant.GREEN,4)
# cv.rectangle(image, (80, 50), (130, 300), constant.GREEN, -1)
# cv.circle(image, (50, 50), 20, constant.BLUE, 3)
# cv.circle(image, (100, 100), 30, constant.RED, -1)

cv.line(image, (0, 0), (300, 300),constant.BLUE, 3)
cv.rectangle(image, (0, 0), (100, 100), constant.RED, 3)
ret, p1, p2 = cv.clipLine((0, 0, 100, 100), (0, 0), (300, 400))
if ret:
    cv.line(image, p1, p2, constant.YELLOW, 3)
    plt.subplot(111)
cv.arrowedLine(image, (200, 50), (30, 50), constant.RED, 3, 8, 0, 0.1)
cv.arrowedLine(image, (50, 120), (200, 120), constant.YELLOW, 3, cv.LINE_AA, 0, 0.3)

# These points define a triangle
pts = np.array([[250, 5], [220, 80], [280, 80]], np.int32)
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
# Print the shapes: this line is not necessary, only for visualization
print("shape of pts {}".format(pts.shape))
# Draw this poligon with True option
cv.polylines(image, [pts], True, constant.CYAN, 3)

shift = 2
factor = 2 ** shift
print("factor: '{}'".format(factor))
cv.circle(image, (int(round(299.99 * factor)), int(round(299.99 * factor))), 300 * factor, constant.RED, 1,8,2)
cv.circle(image, (299, 299), 300, constant.GREEN, 1)
plt.imshow(image_matplotlib)
plt.show()

cv.waitKey(0)
