import cv2
import numpy as np

def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    mean = np.median(blurred)
    min_threshold = 0.66*mean
    max_threshold = 1.33*mean
    res = cv2.Canny(blurred, min_threshold, max_threshold)
    return res