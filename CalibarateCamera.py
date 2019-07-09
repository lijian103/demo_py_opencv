import numpy as np
import matplotlib.pyplot as plt
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 方格的宽度，单位mm
square_size = 27.5

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((9 * 6, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2) * square_size
# objp[:,2:3]=10
# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

images = glob.glob('./frame_name/*.png')
index = 0
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
    print(ret)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (9, 6), corners2, ret)
        cv2.imshow('img' + str(index), img)
        index = index + 1
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
        print(ret)
        print(mtx)
        print(dist)
        print(len(rvecs), rvecs[-1])
        print(len(tvecs), tvecs[-1])

tot_error = 0
for i in range(len(imgpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    tot_error += error
average_error = (tot_error / len(imgpoints)) ** 0.5
print(ret, average_error)

# 畸变矫正部分程序
for fname in images:
    img = cv2.imread(fname)
    rows, cols = img.shape[:2]
    newcamera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (cols, rows), 0)
    img_undistort = cv2.undistort(img, mtx, dist, None, newcamera_mtx)
    x, y, cols, rows = roi
    img_undistort = img_undistort[y:y + rows, x:x + cols]
    print(roi)
    plt.subplot(121), plt.imshow(img), plt.title("img")
    plt.subplot(122), plt.imshow(img_undistort), plt.title("img_undistort")
    plt.show()

# 畸变矫正部分(2)程序
for fname in images:
    img = cv2.imread(fname)
    rows, cols = img.shape[:2]
    newcamera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (cols, rows), 1)
    img_undistort = cv2.undistort(img, mtx, dist, None)
    map_x, map_y = cv2.initUndistortRectifyMap(mtx, dist, None, newcamera_mtx, (cols, rows), 5)
    img_undistort = cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR)
    print(map_x.shape)
    print(map_y)

    plt.subplot(121), plt.imshow(img), plt.title("img")
    plt.subplot(122), plt.imshow(img_undistort), plt.title("img_undistort")
    plt.show()

if cv2.waitKey(1000 * 60) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
