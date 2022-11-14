#!/usr/bin/env python

#import cv2 
import pytesseract
import numpy as np

def get_text_from_image(image: np.ndarray) -> str:
    return pytesseract.image_to_string(image)
