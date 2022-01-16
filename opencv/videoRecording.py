import cv2
import time
import keyboard

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

time.sleep(2)
width= int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

startVideo = False

while(cam.isOpened()):
    ret,frame= cam.read()
    cv2.imshow('webcam', frame)

    if startVideo and ret:
        writer.write(frame)

    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('r'):  # if key 'q' is pressed 
            print('You Start Recording Video')
            startVideo = True
        elif keyboard.is_pressed('p'):
            print('You pause Recording Video')
            startVideo = False
        elif keyboard.is_pressed('s'):
            print('You Stop Recording Video')
            startVideo = False
            break
    except:
        break  # if user pressed a key other than the given key the loop will break

    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    

cam.release()
writer.release()
cv2.destroyAllWindows()