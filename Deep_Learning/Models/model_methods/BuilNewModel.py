import tensorflow as tf
from zipfile import ZipFile
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from datetime import datetime
#############################
#   SETUT DATA
#############################
# file_name = "archive.zip"

# with ZipFile(file_name, 'r') as zip:
#   zip.extractall()
#   print("Done")


#############################
#   SETUT DATA FOR MODEL
#############################
train_dir = 'train'
val_dir = 'test'
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)


print("[UPDATE] STARTING DATA GENERATORS...")
train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(48,48),
        batch_size=32,
        color_mode="grayscale",
        class_mode='categorical')

validation_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=(48,48),
        batch_size=32,
        color_mode="grayscale",
        class_mode='categorical')

print("[UPDATE] DATA GENERATORS DONE.")

#############################
#   SETUT MODEL
#############################
print("[UPDATE] STRTING MODEL SETUP...")


emotion_model = Sequential()
emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(3, activation='softmax')) #Change Outout AMOUNT

print("[UPDATE]MODEL SETUP DONE.")

#############################
#         TRAIN MODEL
#############################
print("[UPDATE] STARTING MODEL TRAINING...")

emotion_model.compile(loss='categorical_crossentropy',optimizer=Adam(learning_rate=0.001, decay=1e-6),metrics=['accuracy'])
emotion_model_info = emotion_model.fit(
        x=train_generator,
        epochs=40,
        )

#Saving the model
# datetime object containing current date and time
now = datetime.now()
name = "emotion_model_3_EMOTIOS" + now.strftime("%d_%m_%Y %H-%M-%S")
emotion_model.save(name + '.h5')