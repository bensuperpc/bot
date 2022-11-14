#!/usr/bin/env python

import numpy as np
#import cv2 as cv
from mss import mss

def get_screenshot(mon : dict = {'left': 0, 'top': 0, 'width': 2560, 'height': 1440}) -> np.ndarray:
    screenshot = np.array(mss().grab(mon))
    
    #screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2RGB)
    #screenshot = screenshot[:, :, ::-1] # BGR to RGB
    return screenshot
