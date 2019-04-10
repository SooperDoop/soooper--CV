# -*- coding: utf-8 -*-

# camera.py

import cv2

class VideoCamera(object):
    

    def __init__(self):
        self.video = cv2.VideoCapture(1)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
#            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        ret, jpeg = cv2.imencode('.jpg', image)
        
        
        return jpeg.tobytes()
