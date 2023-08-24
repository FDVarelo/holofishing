import mss
import cv2 as cv
import numpy as np
import pydirectinput as di
import keyboard
import pyautogui

### Images models.
#INDICATOR = cv.imread('assets/indicator.png', cv.IMREAD_GRAYSCALE) ### Fishing model.
UP = cv.imread('assets/up.png', cv.IMREAD_GRAYSCALE)
DOWN = cv.imread('assets/down.png', cv.IMREAD_GRAYSCALE)
LEFT = cv.imread('assets/left.png', cv.IMREAD_GRAYSCALE)
RIGHT = cv.imread('assets/right.png', cv.IMREAD_GRAYSCALE)
CIRCLE = cv.imread('assets/circle.png', cv.IMREAD_GRAYSCALE)

isFishingLocal = {"top": 270, "left": 1224, "width": 51, "height": 81} ### Fishing mode location.
captureMovNow = {"top": 708, "left": 1121, "width": 106, "height": 96} ### Local to capture the input to do now.

with mss.mss() as sct:
    while keyboard.is_pressed('q') == False: ### hold 'q' to quit.
        ### Verifying if is now on fishing mode
        r,g,b = pyautogui.pixel(1181,696) ### Get one pixel of the arrow above the input now, faster than getting the fishing icon.
        
        ### If is on fishing mode.
        if r == 251 and g == 251 and b == 251: ### Faster than verifying the minMaxLoc and searching similar images.    
                MovNow = np.array(sct.grab(captureMovNow))
                target = cv.cvtColor(MovNow, cv.COLOR_BGRA2GRAY)

                resUp = cv.matchTemplate(target, UP, cv.TM_CCOEFF_NORMED)
                resDown = cv.matchTemplate(target, DOWN, cv.TM_CCOEFF_NORMED)
                resLeft = cv.matchTemplate(target, LEFT, cv.TM_CCOEFF_NORMED)
                resRight = cv.matchTemplate(target, RIGHT, cv.TM_CCOEFF_NORMED)
                resCircle = cv.matchTemplate(target, CIRCLE, cv.TM_CCOEFF_NORMED)

                if (cv.minMaxLoc(resUp)[1] > 0.7):
                    di.press("w")
                elif (cv.minMaxLoc(resDown)[1] > 0.7):
                    di.press("s")
                elif (cv.minMaxLoc(resLeft)[1] > 0.7):
                    di.press("a")
                elif (cv.minMaxLoc(resRight)[1] > 0.7):
                    di.press("d")
                elif (cv.minMaxLoc(resCircle)[1] > 0.7):
                    di.press("space")

        ### Not on fishing mode.
        else:
            di.press("space")
