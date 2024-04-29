import numpy as np
import time
import cv2
from TeleVision import TeleVision

np.set_printoptions(precision=2, suppress=True)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
if not cap.isOpened():
    print("Error: Unable to open camera")
    exit()

tv = TeleVision((640, 480), stereo=True)

while True:
    start = time.time()
    ret, frame = cap.read()
    if ret:
        print(f'Frame shape: {frame.shape}')
        left_frame = frame[:, :frame.shape[1]//2]
        right_frame = frame[:, frame.shape[1]//2:]
        combined_frame = np.vstack((left_frame, right_frame))
        rgb_frame = cv2.cvtColor(combined_frame, cv2.COLOR_BGR2RGB)
        tv.modify_shared_image(rgb_frame)
    end = time.time()
    
cap.release()
