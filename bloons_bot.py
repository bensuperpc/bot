#!/usr/bin/env python

import time
import json

# import pyautogui
from pynput.mouse import Button, Controller

# Cursor position does not sync his position if move during click_count
def mouse_click(posx: int = None, posy: int = None, click_count: int = 1, button: Button = Button.left, mouse: Controller = Controller(), delay: float = 0.8, interval: float = 0.4):
    time.sleep(delay)
    if posx is not None and posy is not None:
        mouse.position = (posx, posy)
    time.sleep(interval)
    for i in range(0, click_count):
        mouse.click(button, 1)
        time.sleep(interval)

# Cursor position does not sync his position if move during scroll_count
def mouse_scroll(posx: int = None, posy: int = None, scroll_count: int = 1, scrollx: int = 0, scrolly: int = 0, button: Button = Button.scroll_up, mouse: Controller = Controller(), delay: float = 0.8, interval: float = 0.4):
    time.sleep(delay)
    if posx is not None and posy is not None:
        mouse.position = (posx, posy)
    time.sleep(interval)
    for i in range(0, scroll_count):
        mouse.scroll(scrollx, scrolly)
        time.sleep(interval)


def main():
    data = None
    time.sleep(4.0)
    with open("bloons_bot.json", "r") as f:
        data = json.load(f)

    for action in data.get("action"):
        print(action.get("information"))

        if action.get("type") == "click":
            mouse_click(
                posx=action.get("posx"),
                posy=action.get("posy"),
                click_count=action.get("click_count"),
                delay=action.get("delay"),
                interval=action.get("interval"),
            )
        elif action.get("type") == "scroll":
            mouse_scroll(
                posx=action.get("posx"),
                posy=action.get("posy"),
                scrollx=action.get("scrollx"),
                scrolly=action.get("scrolly"),
                delay=action.get("delay"),
                interval=action.get("interval"),
            )
        elif action.get("type") == "wait":
            time.sleep(action.get("delay"))
        else:
            print("Unknown action type: {}".format(action.get("type")))

    # with open("bloons_bot.json", "w") as f:
    #     json.dump(data, f, indent=4)

    main()


if __name__ == "__main__":
    main()
