# -*- coding: utf-8 -*-
from re import X
import pyautogui as pg
from PIL import ImageGrab
from functools import partial
import screeninfo
import time

img_moneybox1 = r'C:\python\image_processing\money_tree\moneybox1.png'
img_moneybox2 = r'C:\python\image_processing\money_tree\moneybox2.png'
img_close = r'C:\python\image_processing\money_tree\close.png'
img_x1 = r'C:\python\image_processing\money_tree\x1.png'


def find_and_clik(img):
    Flag = False
    confi = 0.9
    
    find_img = pg.locateOnScreen(img, confidence=confi)
    time.sleep(0.01)

    if find_img != None:
        time.sleep(0.01)
        pg.click(find_img, clicks=1, duration=0.1)
        Flag = True

    return Flag


if __name__ =='__main__':

    try:
        while True:
            Flag = False
            Flag = find_and_clik(img_moneybox1)
            find_and_clik(img_x1)
            time.sleep(0.5)
            if find_and_clik(img_moneybox2) == False:
                time.sleep(0.5)
                find_and_clik(img_close)

        

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass