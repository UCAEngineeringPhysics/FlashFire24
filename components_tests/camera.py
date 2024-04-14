import cv2
from picamera2 import Picamera2
from time import time

cv2.startWindowThread()
cam = Picamera2()
cam.configure(cam.create_preview_configuration(main={"format": 'RGB888', "size": (120, 160)}))
cam.start()

# Init timer for FPS computing
start_stamp = time()
frame_counts = 0
ave_frame_rate = 0.
while True:
    frame = cam.capture_array()
    # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Camera", frame)
    frame_counts += 1
    # Log frame rate
    since_start = time() - start_stamp
    frame_rate = frame_counts / since_start
    print(f"frame rate: {frame_rate}")    
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
