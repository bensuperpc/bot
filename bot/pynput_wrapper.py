#!/usr/bin/env python

import time

# import pyautogui
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

# Cursor position does not sync his position if move during click_count
def mouse_click(posx: int = None, posy: int = None, click_count: int = 1, button: Button = Button.left, mouse: MouseController = MouseController(), delay: float = 0.8, interval: float = 0.4):
    time.sleep(delay)
    if posx is not None and posy is not None:
        mouse.position = (posx, posy)
    time.sleep(interval)
    for i in range(0, click_count):
        mouse.click(button, 1)
        time.sleep(interval)

# Cursor position does not sync his position if move during scroll_count
def mouse_scroll(posx: int = None, posy: int = None, scrollx: int = 0, scrolly: int = 0, scroll_count: int = 1, button: Button = Button.scroll_up, mouse: MouseController = MouseController(), delay: float = 0.8, interval: float = 0.4):
    time.sleep(delay)
    if posx is not None and posy is not None:
        mouse.position = (posx, posy)
    time.sleep(interval)
    for i in range(0, scroll_count):
        mouse.scroll(scrollx, scrolly)
        time.sleep(interval)

def keyboard_press(key: Key = Key.enter, keyboard: KeyboardController = KeyboardController(), press_count: int = 1, delay: float = 0.8, interval: float = 0.4):
    time.sleep(delay)
    for i in range(0, press_count):
        keyboard.press(key)
        time.sleep(interval)
        keyboard.release(key)
        time.sleep(interval)