import numpy as np
import time
import cv2
from TeleVision import OpenTeleVision

np.set_printoptions(precision=2, suppress=True)

resolution = (720, 1280)  # Desired resolution

# Create a VideoCapture object and open the input file
cap = cv2.VideoCapture(0)  # 0 is usually the default camera

# Set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[1])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[0])
cap.set(cv2.CAP_PROP_FPS, 60)  # Set FPS to 60

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Unable to open camera")
    exit()

tv = OpenTeleVision(resolution)

while True:
    start = time.time()

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Our operations on the frame come here
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Assume the camera only provides one view, so we double it for the shared image
        tv.modify_shared_image(np.vstack((rgb_frame, rgb_frame)))

    end = time.time()

# When everything done, release the capture
cap.release()
