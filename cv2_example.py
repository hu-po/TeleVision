import numpy as np
import time
import cv2
from TeleVision import TeleVision

np.set_printoptions(precision=2, suppress=True)

resolution = (720, 1280)

# Create a VideoCapture object and open the input file
cap = cv2.VideoCapture(0)  # 0 is usually the default camera

# Set the resolution
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[1])
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[0])
cap.set(cv2.CAP_PROP_FPS, 60)  # Set FPS to 60

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Unable to open camera")
    exit()

tv = TeleVision(resolution, stereo=True)

while True:
    start = time.time()
    ret, frame = cap.read()
    print(f'Frame shape: {frame.shape}')
    if ret:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        tv.modify_shared_image(rgb_frame)
    end = time.time()
    
cap.release()
