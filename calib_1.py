import time
import os
import cv2
import numpy
import matplotlib.pyplot as plot


def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i) # 取文件绝对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)


# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture(0)
# 根据摄像头设置IP及rtsp端口
url = "rtsp://169.254.109.52:554/ch1/1"

# 读取视频流
cap = cv2.VideoCapture(url)
# Check if camera opened successfully
if capture.isOpened() is False:
    print("Error opening the camera")
# Read until video is completed
while capture.isOpened():
    # Capture frame-by-frame from the camera
    ret, frame = capture.read()
    if ret is True:
        # Display the captured frame:
        cv2.imshow('Input frame from the camera', frame)
        # Convert the frame captured from the camera to grayscale:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the grayscale frame:
        cv2.imshow('Grayscale input camera', gray_frame)
        # Press q on keyboard to exit the program
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(20) & 0xFF == ord('r'):
            del_file("./frame_name")
            del_file("./gray_frame_name")

        # Press c on keyboard to save current frame
        elif cv2.waitKey(20) & 0xFF == ord('s'):
            frame_name = "camera_frame_{}.png".format(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())))
            gray_frame_name = "grayscale_camera_frame_{}.png".format(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())))
            cv2.imwrite("./frame_name/"+frame_name, frame)
            cv2.imwrite("./gray_frame_name/"+gray_frame_name, gray_frame)
    # Break the loop
    else:
        break
# Release everything:
capture.release()
cv2.destroyAllWindows()


