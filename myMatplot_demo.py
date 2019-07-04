import numpy as np
import numpy.matlib
from matplotlib import pyplot as plt
import  cv2
img_OpenCV = cv2.imread('./1.JPg')
b, g, r = cv2.split(img_OpenCV)
img_matplotlib = cv2.merge([r, g, b])
plt.figure("Image",figsize=(10,5)) #设置窗口大小
plt.suptitle('Multi_Image') # 图片名称
plt.subplot(2,3,1), plt.title('image')
plt.imshow(img_matplotlib), plt.axis('on')
plt.xlabel("x_lable")
plt.ylabel("y_lable")
plt.subplot(2,3,2), plt.title('gray')
img_gray=cv2.cvtColor(img_OpenCV,cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray,cmap='gray'), plt.axis('off') #这里显示灰度图要加cmap

plt.figure("plot")
x= np.arange(0,3*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.subplot(3,  3,  1)
plt.title("myMatplot_demo1优酷")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y_sin,"--r")

plt.plot(x,y_cos,"-b")
plt.show()

plt.subplot(3, 3,  2)
x =  [5,8,10]
y =  [12,16,6]
x2 =  [6,9,11]
y2 =  [6,15,7]
plt.bar(x, y, align =  'center')
plt.bar(x2, y2, color =  'g', align =  'center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

plt.subplot(3, 3,  3)
# a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
# np.histogram(a,bins =  [0,20,40,60,80,100])
# hist,bins = np.histogram(a,bins =  [0,20,40,60,80,100])
# print (hist)
# print (bins)
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a, bins =  [0,20,40,60,80,100])
plt.title("histogram")
plt.show()



import matplotlib.pyplot as plt
plt.figure("plot——new")
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
plt.plot(x_data, y_data, color = 'red', linewidth = 2.0,
    linestyle = '--', label='Java基础')
plt.plot(x_data, y_data2, color = 'blue', linewidth = 3.0,
    linestyle = '-.', label='C基础')
import matplotlib.font_manager as fm
# 使用Matplotlib的字体管理器加载中文字体
my_font=fm.FontProperties(fname="C:\Windows\Fonts\simkai.ttf")
# 调用legend函数设置图例
plt.legend(loc='best')
# 设置两条坐标轴的名字
plt.xlabel("年份")
plt.ylabel("教程销量")
# 设置数据图的标题
plt.title('C语言中文网的历年销量')
# 设置Y轴上的刻度值
# 第一个参数是点的位置，第二个参数是点的文字提示
plt.yticks([50000, 70000, 100000],
    [r'挺好', r'优秀', r'火爆'])
# 调用show()函数显示图形
plt.show()