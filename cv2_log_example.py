import numpy as np
import time
import cv2
from TeleVision import TeleVision
import matplotlib.pyplot as plt

np.set_printoptions(precision=2, suppress=True)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
if not cap.isOpened():
    print("Error: Unable to open camera")
    exit()

tv = TeleVision((480, 640), stereo=True)

# Initialize lists to store time data
camera_capture_times = []
image_processing_times = []
hands_times = []
head_matrix_times = []

try:
    while True:
        start_cam = time.time()
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        end_cam = time.time()

        # Camera capture time
        camera_capture_time = end_cam - start_cam
        camera_capture_times.append(camera_capture_time)

        # Image processing
        start_img_proc = time.time()
        width = frame.shape[1]
        left_frame = frame[:, :width//2]
        right_frame = frame[:, width//2:]
        frame = np.vstack((left_frame, right_frame))
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        tv.modify_shared_image(rgb_frame)
        end_img_proc = time.time()

        # Image processing time
        img_proc_time = end_img_proc - start_img_proc
        image_processing_times.append(img_proc_time)

        # Hand detection
        start_hands = time.time()
        left_hand = tv.left_hand()
        right_hand = tv.right_hand()
        end_hands = time.time()
        hands_proc_time = end_hands - start_hands
        hands_times.append(hands_proc_time)

        # Head matrix calculation
        start_head_matrix = time.time()
        head_matrix = tv.head_matrix()
        end_head_matrix = time.time()
        head_matrix_proc_time = end_head_matrix - start_head_matrix
        head_matrix_times.append(head_matrix_proc_time)

        # Example break condition for testing (e.g., run for 100 frames)
        if len(camera_capture_times) >= 100:
            break

finally:
    cap.release()

    # Plotting the times
    plt.figure(figsize=(10, 6))
    plt.plot(camera_capture_times, label='Camera Capture Time')
    plt.plot(image_processing_times, label='Image Processing Time')
    plt.plot(hands_times, label='Hands Detection Time')
    plt.plot(head_matrix_times, label='Head Matrix Calculation Time')
    plt.xlabel('Frame')
    plt.ylabel('Time (seconds)')
    plt.title('Timing Analysis')
    plt.legend()
    plt.show()
