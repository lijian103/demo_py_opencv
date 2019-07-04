import numpy as np
import cv2
import timeit
import time
e1 = cv2.getTickCount()
num=0
for i in range(1000):
    num=num+1
# your code execution
e2 = cv2.getTickCount()
delta_time = (e2 - e1)/ cv2.getTickFrequency()
print(delta_time)

#测试时间是ms级别，不够精确
tm1=time.time()
print(tm1)
for i in range(1000):
    num=num+1
tm2=time.time()
print(tm2)
time_delta=tm2-tm1
print(time_delta)

img = cv2.imread('m1.png')
# %timeit z = cv2.countNonZero(img)
#
# %timeit z = np.count_nonzero(img)
