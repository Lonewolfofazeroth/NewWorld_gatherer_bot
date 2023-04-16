import pyautogui as pg
import time
from pynput.keyboard import Key, Controller


keyboard=Controller()
def conf(img=None):
    match_=True
    for c in range(10,6,-1):
        c = c / 10
        match_=pg.locateCenterOnScreen(img,confidence=c)
        if match_:
            print(c)
            return(match_)
    return(None)

while True:
    # time.sleep(1)
    while conf("img/E.png"):
        keyboard.tap("e")
    keyboard.tap("q")
    
