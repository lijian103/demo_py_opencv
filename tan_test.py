import numpy as np
from matplotlib import pyplot as plt
import matplotlib
x_axis=np.arange(0,np.pi*4,0.005)
y_axis=np.tan(x_axis)
x_arctan=np.arctan(y_axis)

plt.xlabel("x_lable")
plt.ylabel("y_lable")
plt.subplot(3,  3,  1)
plt.plot(x_axis,y_axis)
plt.subplot(3,  3, 2)
plt.plot(x_axis)
plt.subplot(3,  3, 3)
plt.plot(x_arctan)
plt.subplot(3,  3, 4)
plt.plot(np.unwrap(2 * x_arctan) / 2)
plt.show()
