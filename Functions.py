import cv2
import os
import numpy as np



def imageTake():
    path = "D:/AUA Class of 2023/Semester 2/Introduction to Programming/Individual project code/Spectral Analysis/Images"
    path1 = "D:/AUA Class of 2023/Semester 2/Introduction to Programming/Individual project code/Spectral Analysis/BMP"
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite(os.path.join(path, 'spectrum' + '.png'), image)
    cv2.imwrite(os.path.join(path1, 'spectrum1' + '.png'), image)
    del camera
