# import the opencv library
import cv2
import keyboard
import time
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
if not vid.isOpened():
    raise ValueError("Unable to open video source", 0)

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    if keyboard.is_pressed('c'):  # if key 'q' is pressed 
        photo_name = "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"

        cv2.imwrite(photo_name, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        print('You Captured a photo')
        startVideo = True
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()