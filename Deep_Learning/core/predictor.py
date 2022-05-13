"""
Team: Team Fresh
Author: Samuel Silva
Class: PI0919
Creation_Date: 13/10/2021

Methods to predict an emotion using the model
"""

import os

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image

# Local imports
import config

# CONSTANTS

MODEL = os.path.join(config.MODELS_DIR, config.MODEL_NAME)





# GLOBAL VARIABLES


def predictor_load_model():
    """
    Loads the model and returns it
    @return: Deep Learning Keras Model
    """
    return load_model(MODEL)


def get_new_prediction(model, x):
    """
    Recieves an Image Numpy Array as parameter
    @param model: Deep Learning Keras Model
    @param x: of image pixels -> numpy Array []
    @return: str -> prediction result
    """

    print("[PREDICTION] Starting Prediction...")
    emotion_prediction = model.predict(x)
    print("[PREDICTION] Predicted.")
    p_index = int(np.argmax(emotion_prediction))
    prediction = config.EMOTION_DICT[p_index]
    print("[PREDICTION RESULT] :: " + prediction["Emotion"])

    return prediction


def convert_img_to_numpyArray(img_path):
    """
    Converts an Image to a numpy Array in the format used for predictions
    @param img_path: str ->  path of the image
    @return: numpy array []
    """
    img = keras_image.load_img(img_path, color_mode="grayscale", target_size=config.IMAGE_SIZE)

    x = keras_image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255  # Values from 0 to 1 for easier calculations

    return x


def get_new_prediction_from_image(model, image_to_predict):
    """
    Receives an Image as parameter and creates a prediction using the model
    @param model: Deep Learning Keras Model
    @param image_to_predict: str -> of image we want to predict
    @return: str -> prediction result
    """
    """
   

    :param image: Image or numpy Array
    :return :
    """
    # Prepare Image
    x = convert_img_to_numpyArray(image_to_predict)
    # Start Prediction Process
    prediction = get_new_prediction(model, x)

    return prediction


def get_new_prediction_from_numpy_image(model, np_img):
    """
    Receives an images as a numpy array and return a prediction
    @param model:
    @param np_img:
    @return:
    """

    # Prepare Image
    x = np.expand_dims(np_img, axis=0)
    x /= 255  # Values from 0 to 1 for easier calculations

    # Start Prediction Process
    prediction = get_new_prediction(model, x, np_img)

    # Return result emotion
    return prediction


def get_new_prediction_from_images(images):
    """
    Receives an array of Images as parameter and creates a prediction using the model

    :param images: Array[Image1, Image2]
    :return :
    """
    pass
