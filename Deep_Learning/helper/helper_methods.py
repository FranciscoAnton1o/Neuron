"""
Author: Samuel Silva
Class: PI0919
Creation_Date: 13/10/2021

helper Methods 
"""
import matplotlib as plt
import numpy as np


def emotion_analysis(emotions, img):
    objects = ('happy', 'neutral', 'sad')
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, emotions, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotion')
    plt.show()
    plt.imshow(img)
    plt.show()
