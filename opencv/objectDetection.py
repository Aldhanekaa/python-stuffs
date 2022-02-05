import tkinter
from tkinter import messagebox
import cv2
import PIL.Image, PIL.ImageTk
import time


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # open video source (by default this will try to open the computer webcam)
        self.vid = VideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 1
        self.update()

        self.window.mainloop()
    
    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            photo_name = "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
            photosaved = cv2.imwrite(photo_name, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        messagebox.showinfo("Information", f"Photo Saved {photo_name}")

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imshow('webcam', frame)

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            # Draw rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Display the output
            cv2.imshow('img', frame)

            cv2.imwrite('cat.jpeg', frame)  
            # image = cv2.imread('cat.jpeg')
            # box, label, count = cv.detect_common_objects(image)
            # output = draw_bbox(image, box, label, count)
            # print(output)


            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)

class VideoCapture:
    def __init__(self, video_source=0):
        # open the video source 
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
        
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, frame)
            else:
                return (ret, None)
        else:
            return (None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

App(tkinter.Tk(), "Tkinter X OpenCV")