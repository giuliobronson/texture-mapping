import numpy as np
import cv2

class ClickHandler:

    def __init__(self):
        self.points = []

    def capture_coordinates(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN: 
            self.points.append((x, y))

    def get_coordinates(self):
        return self.points