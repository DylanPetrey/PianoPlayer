# works on the website:
# ffffa

import numpy as np
from PIL import ImageGrab
import cv2
import time
from pynput.keyboard import Controller

coords = [430, 166, 830, 766]       #Bounds of the game board
keyboard = Controller()             #Presses keys onto the game

# This function takes in the screen and then presses a key if a black tile
# is at the appropriate height
# works by checking each column for a tile at a certain height and deciding where to press
def clickOnBlock(screen):
    global coords

    #loop that iterates over each column
    for i in range(4):
        # Where to check for a tile
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        x = i * width // 4 + width // 8     # sets x val to the middle of one of the columns
        y = 17 * height // 20               # set y value to check for tile

        # checks if current tile is black and then presses a key based on the column
        if screen[y][x] < 40 and screen[y+2][x] < 40:
            if i == 0:
                keyboard.press('a')
                keyboard.release('a')
            elif i == 1:
                keyboard.press('s')
                keyboard.release('s')
            elif i == 2:
                keyboard.press('d')
                keyboard.release('d')
            elif i == 3:
                keyboard.press('f')
                keyboard.release('f')
            return


# endless loop
while True:
    # takes screenshots of the game and converts it to grayscale
    screen = np.array(ImageGrab.grab(bbox=coords))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    clickOnBlock(screen)
    time.sleep(0.12)           # slows down the program so it doesnt go too fast
