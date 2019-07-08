import numpy as np
from matplotlib import pyplot as plt
import cv2

Image_rows = 1140
Image_cols = 912


def cos_wave(initial_phase=0, Period=70):
    """
    """
    x_axis_cos = np.linspace(initial_phase, 2 * np.pi * Period + initial_phase, Image_cols)
    x_axis_col = x_axis_cos.reshape(Image_cols, 1)
    x_axis_temp = np.concatenate((x_axis_col, x_axis_col), axis=1)
    x_axis_image = np.concatenate((x_axis_temp, x_axis_col), axis=1).reshape(1, Image_cols, 3)
    y_axis = 90 * np.cos(x_axis_image) + 120
    cos_wave = np.zeros((Image_rows, Image_cols, 3), dtype="uint8")
    cos_wave[:] = y_axis
    plt.figure("cos_wave" + "_initial_phase_" + str(initial_phase) + "_Period_" + str(Period))
    plt.xlabel("x")
    plt.ylabel("y")
    y_axis1 = 90 * np.cos(x_axis_cos) + 120
    plt.plot(x_axis_cos, y_axis1)
    cv2.imwrite(
        "./cos_pictures/" + "cos_wave" + "_Period_" + str(Period) + "_initial_phase_" + str(initial_phase) + ".bmp",
        cos_wave)
    cv2.imshow("cos_wave" + "_Period_" + str(Period) + "_initial_phase_" + str(initial_phase), cos_wave)


def cos_wave_gray(initial_phase=0, Period=70):
    """
    不需要此函数，投影仪需要24bit图片输入，cvt函数转换为灰度图也不可以。
    """
    x_axis_cos = np.linspace(initial_phase, 2 * np.pi * Period + initial_phase, Image_cols)
    y_axis = 90 * np.cos(x_axis_cos) + 120
    cos_wave = np.zeros((Image_rows, Image_cols), dtype="uint8")
    cos_wave[:] = y_axis
    plt.figure("cos_wave" + "_initial_phase_" + str(initial_phase) + "_Period_" + str(Period))
    plt.xlabel("x")
    plt.ylabel("y")
    y_axis1 = 90 * np.cos(x_axis_cos) + 120
    plt.plot(x_axis_cos, y_axis1)
    cv2.imwrite(
        "./cos_pictures_gray/" + "cos_wave_gray" + "_Period_" + str(Period) + "_initial_phase_" + str(
            initial_phase) + ".bmp",
        cos_wave)
    cv2.imshow("cos_wave_gray" + "_Period_" + str(Period) + "_initial_phase_" + str(initial_phase), cos_wave)


def sin_wave(initial_phase=0, Period=70):
    """
    """
    x_axis_sin = np.linspace(initial_phase, 2 * np.pi * Period + initial_phase, Image_cols)
    x_axis_col = x_axis_sin.reshape(Image_cols, 1)
    x_axis_temp = np.concatenate((x_axis_col, x_axis_col), axis=1)
    x_axis_image = np.concatenate((x_axis_temp, x_axis_col), axis=1).reshape(1, Image_cols, 3)
    y_axis = 90 * np.sin(x_axis_image) + 120
    sin_wave = np.zeros((Image_rows, Image_cols, 3), dtype="uint8")
    sin_wave[:] = y_axis
    plt.figure(str(initial_phase))
    plt.xlabel("x")
    plt.ylabel("y")
    y_axis1 = 90 * np.sin(x_axis_sin) + 120
    plt.plot(x_axis_sin, y_axis1)
    cv2.imwrite("./sin_pictures/" + "sin_wave" + str(initial_phase) + ".bmp", sin_wave)
    cv2.imshow('sin_wave' + str(initial_phase), sin_wave)


def sin_wave_rotate(initial_phase=0, Period=40):
    """
    """
    x_axis_sin = np.linspace(initial_phase, 2 * np.pi * Period + initial_phase, Image_cols)
    x_axis_col = x_axis_sin.reshape(Image_cols, 1)
    x_axis_temp = np.concatenate((x_axis_col, x_axis_col), axis=1)
    x_axis_image = np.concatenate((x_axis_temp, x_axis_col), axis=1).reshape(1, Image_cols, 3)
    y_axis = 90 * np.sin(x_axis_image) + 120
    sin_wave = np.zeros((Image_rows, Image_cols, 3), dtype="uint8")
    sin_wave[:] = y_axis
    height, width = sin_wave.shape[:2]
    M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), -45, 1)
    dst_image = cv2.warpAffine(sin_wave, M, (width, height))
    cv2.imshow('sin_wave_rotate' + str(initial_phase), dst_image)


def fringe_wave(initial_phase=0, Period=40):
    """
    """
    x_axis_sin = np.linspace(initial_phase, 2 * np.pi * Period + initial_phase, Image_cols)
    x_axis_col = x_axis_sin.reshape(Image_cols, 1)
    x_axis_temp = np.concatenate((x_axis_col, x_axis_col), axis=1)
    x_axis_image = np.concatenate((x_axis_temp, x_axis_col), axis=1).reshape(1, Image_cols, 3)
    y_axis = np.sin(x_axis_image)
    for i in range(1):
        for j in range(Image_cols):
            for d in range(3):
                if y_axis[i][j][d] >= 0:
                    y_axis[i][j][d] = 255
                else:
                    y_axis[i][j][d] = 0
    sin_wave = np.zeros((Image_rows, Image_cols, 3), dtype="uint8")
    sin_wave[:] = y_axis
    cv2.imshow('fringe_wave' + str(initial_phase), sin_wave)


def fringe_wave_rotate(initial_phase=0, Period=40):
    """
    """
    x_axis_sin = np.linspace(initial_phase, 2 * np.pi * Period + initial_phase, Image_cols)
    x_axis_col = x_axis_sin.reshape(Image_cols, 1)
    x_axis_temp = np.concatenate((x_axis_col, x_axis_col), axis=1)
    x_axis_image = np.concatenate((x_axis_temp, x_axis_col), axis=1).reshape(1, Image_cols, 3)
    y_axis = np.sin(x_axis_image)
    for i in range(1):
        for j in range(Image_cols):
            for d in range(3):
                if y_axis[i][j][d] >= 0:
                    y_axis[i][j][d] = 255
                else:
                    y_axis[i][j][d] = 0
    sin_wave = np.zeros((Image_rows, Image_cols, 3), dtype="uint8")
    sin_wave[:] = y_axis
    sin_wave_rotate = np.transpose(sin_wave, (1, 0, 2))
    # sin_wave_rotate=cv2.cvtColor(sin_wave_rotate, cv2.COLOR_BGR2GRAY)
    cv2.imshow('fringe_wave_rotate' + str(initial_phase), sin_wave_rotate)


def fringe_wave_cross(initial_phase=0, Period=40):
    """
    """
    x_axis_sin = np.linspace(initial_phase, 2 * np.pi * Period + initial_phase, Image_rows)
    x_axis_col = x_axis_sin.reshape(Image_rows, 1)
    x_axis_temp = np.concatenate((x_axis_col, x_axis_col), axis=1)
    x_axis_image = np.concatenate((x_axis_temp, x_axis_col), axis=1).reshape(1, Image_rows, 3)
    y_axis = np.sin(x_axis_image)
    for i in range(1):
        for j in range(Image_rows):
            for d in range(3):
                if y_axis[i][j][d] >= 0:
                    y_axis[i][j][d] = 255
                else:
                    y_axis[i][j][d] = 0
    sin_wave = np.zeros((Image_rows, Image_rows, 3), dtype="uint8")
    sin_wave[:] = y_axis
    sin_wave_rotate = np.transpose(sin_wave, (1, 0, 2))
    # sin_wave_rotate=cv2.cvtColor(sin_wave_rotate, cv2.COLOR_BGR2GRAY)
    sin_wave_cross = np.zeros((Image_rows, Image_rows, 3), dtype="uint8")
    for i in range(Image_rows):
        for j in range(Image_rows):
            for d in range(3):
                if sin_wave_rotate[i][j][d] > 0 or sin_wave[i][j][d] > 0:
                    sin_wave_cross[i][j][d] = 255
                else:
                    sin_wave_cross[i][j][d] = 0
    cv2.imshow('fringe_wave_cross' + str(initial_phase), sin_wave_cross)


def fringe_wave_grid(initial_phase=0, Period=40):
    """
    """
    x_axis_sin = np.linspace(initial_phase, 2 * np.pi * Period + initial_phase, Image_rows)
    x_axis_col = x_axis_sin.reshape(Image_rows, 1)
    x_axis_temp = np.concatenate((x_axis_col, x_axis_col), axis=1)
    x_axis_image = np.concatenate((x_axis_temp, x_axis_col), axis=1).reshape(1, Image_rows, 3)
    y_axis = np.sin(x_axis_image)
    for i in range(1):
        for j in range(Image_rows):
            for d in range(3):
                if y_axis.item(i, j, d) >= 0:
                    y_axis.itemset((i, j, d), 255)
                else:
                    y_axis.itemset((i, j, d), 0)
    sin_wave = np.zeros((Image_rows, Image_rows, 3), dtype="uint8")
    sin_wave[:] = y_axis
    sin_wave_rotate = np.transpose(sin_wave, (1, 0, 2))
    # sin_wave_rotate=cv2.cvtColor(sin_wave_rotate, cv2.COLOR_BGR2GRAY)
    sin_wave_cross = np.zeros((Image_rows, Image_rows, 3), dtype="uint8")
    for i in range(Image_rows):
        for j in range(Image_rows):
            for d in range(3):
                if sin_wave_rotate.item(i, j, d) == sin_wave.item(i, j, d):
                    sin_wave_cross.itemset((i, j, d), 0)
                else:
                    sin_wave_cross.itemset((i, j, d), 255)
    sin_wave_cross_1 = sin_wave_cross[0:Image_rows, 0:Image_cols]
    cv2.imwrite("./sin_pictures/" + "wave_grid" + str(initial_phase) + ".bmp", sin_wave_cross_1)
    cv2.imshow('fringe_wave_grid' + str(initial_phase), sin_wave_cross_1)


if __name__ == "__main__":
    # cos_wave(0,70);
    # cos_wave(0,64);
    # cos_wave(0, 59);
    # sin_wave(np.pi/2)
    # sin_wave(np.pi)
    # sin_wave(3*np.pi / 2)
    # sin_wave_rotate(0)
    # fringe_wave(0)
    # fringe_wave_rotate(0)
    # fringe_wave_cross(0,10)
    # fringe_wave_grid(0,10)

    cos_wave(initial_phase=0, Period=70)
    cos_wave(initial_phase=-np.pi * 2 / 3, Period=70)
    cos_wave(initial_phase=np.pi * 2 / 3, Period=70)

    cos_wave(initial_phase=0, Period=64)
    cos_wave(initial_phase=-np.pi * 2 / 3, Period=64)
    cos_wave(initial_phase=np.pi * 2 / 3, Period=64)

    cos_wave(initial_phase=0, Period=59)
    cos_wave(initial_phase=-np.pi * 2 / 3, Period=59)
    cos_wave(initial_phase=np.pi * 2 / 3, Period=59)

    cos_wave(initial_phase=0, Period=1)
    cos_wave(initial_phase=-np.pi * 2 / 3, Period=1)
    cos_wave(initial_phase=np.pi * 2 / 3, Period=1)

    cos_wave(initial_phase=0, Period=5)
    cos_wave(initial_phase=-np.pi * 2 / 3, Period=5)
    cos_wave(initial_phase=np.pi * 2 / 3, Period=5)

    cos_wave(initial_phase=0, Period=6)
    cos_wave(initial_phase=-np.pi * 2 / 3, Period=6)
    cos_wave(initial_phase=np.pi * 2 / 3, Period=6)

    plt.show()
    cv2.waitKey(0)
