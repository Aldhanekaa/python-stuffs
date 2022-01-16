import numpy as np
import cv2

def gstreamer_pipeline(
    capture_width=640,
    capture_height=480,
    display_width=640,
    display_height=480,
    framerate=21,
    flip_method=0,
):
    return (
        "nvarguscamerasrc! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
if cap.isOpened():
    indow_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
    while cv2.getWindowProperty("CSI Camera", 0) >= 0:
        ret, frame = cap.read()

        cv2.imshow('CSI Camera',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
else:
    print('Cannot open camera')


cap.release()
cv2.destroyAllWindows()
