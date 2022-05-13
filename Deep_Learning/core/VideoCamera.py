"""
Team: Team Fresh
Author: Samuel Silva
Class: PI0919
Creation_Date: 15/10/2021

VideoCamera Class used
"""

import cv2
import time
import os
from PIL import Image

# Local Module Imports
from .predictor import get_new_prediction_from_image
import config


ds_factor = 0.6


def prepare_frame_for_stream(frame):
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor,
                       interpolation=cv2.INTER_AREA)

    # encode OpenCV raw frame to jpeg and displaying it
    ret, jpeg = cv2.imencode('.jpeg', frame)
    return ret, jpeg


def start_Test(camera):
    if not os.path.exists(config.IMAGES_DIR):
        os.mkdir(config.IMAGES_DIR)
    start_time = time.time()
    while True:
        new_frame, is_face_detected = camera.get_frame(start_time)
        cv2.imshow("frame", new_frame)
        if is_face_detected:
            start_time = time.time()

        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


class VideoCamera:
    def __init__(self, model):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.cap = cv2.VideoCapture(0)
        self.model = model
        self.is_face_detected = False

    def __del__(self):
        # releasing camera
        self.cap.release()

    def get_frame(self, time_since_face):
        """
        Get a frame from the webCam
        @param time_since_face: float -> time since a face was detected
        @return: bytes , bool
        """

        # Capture frame-by-frame
        ret, new_frame = self.cap.read()
        new_frame = self.check_for_faces(new_frame, time_since_face)

        # ret, jpeg = prepare_frame_for_stream(new_frame)
        # return jpeg, self.is_face_detected
        return new_frame, self.is_face_detected

    def check_for_face(self):
        pass

    def check_for_faces(self, new_frame, time_since_face):

        # to detect faces in video
        gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)  # Convert Image to GraySacle
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        """
        If there is a face, time restarts to the present moment
        If there are no faces detected and has past X time since last face was seen
        we show a message saying there are no faces detected 
        """

        self.is_face_detected = False
        if len(faces) > 0:
            self.is_face_detected = True
        elif time.time() - time_since_face >= 3.0:
            cv2.putText(new_frame, "NO FACE NO CASE", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        counter = 0
        for (x, y, w, h) in faces:
            """
            Save just the rectangle faces in SubRecFaces
            and use to predict    
            """
            counter += 1
            face_img = gray[y:y + h, x:x + w]
            face_img = cv2.resize(face_img, config.IMAGE_SIZE)  # np Array

            # SAVE IMAGE
            new_face_img = Image.fromarray(face_img)
            image_name = f"Image{counter}.jpg"
            new_face_img.save(os.path.join(config.IMAGES_DIR, image_name))

            new_img_path = os.path.join(config.IMAGES_DIR, image_name)
            prediction_result = get_new_prediction_from_image(self.model, new_img_path)

            cv2.rectangle(new_frame, (x, y), (x + w, y + h), (0, 128, 255), 2)
            cv2.rectangle(new_frame, (x, y - 40), (x + w, y), (255, 0, 0), -1)
            cv2.putText(new_frame, prediction_result["Emotion"], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        return new_frame
