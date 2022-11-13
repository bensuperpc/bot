#!/usr/bin/env python

import time

# import pyautogui
from pynput.mouse import Button, Controller

def mouse_click(posx: int = None, posy: int = None, click_count: int = 1, button: Button = Button.left, mouse: Controller = Controller()):
    time.sleep(0.8)
    if posx is not None and posy is not None:
        mouse.position = (posx, posy)
    time.sleep(0.4)
    for i in range(0, click_count):
        mouse.click(button, 1)
        time.sleep(0.4)

def main():
    mouse = Controller()

    time.sleep(4.0)

    # On Main Menu, click on "Play"
    print("Click on Play")
    mouse_click(1109, 1227)

    # On Map Selection, click on "Expert"
    print("Click on Expert")
    mouse_click(1795, 1290)

    # On Map Selection, click on "Inferno"
    print("Click on Inferno")
    mouse_click(714, 757)

    # On Map difficulty, click on "Easy"
    print("Click on Easy")
    mouse_click(828, 608)

    # On Easy difficulty, click on "Deflation"
    print("Click on Deflation")
    mouse_click(1703, 595)

    # Wait for the game to load
    time.sleep(3.0)

    # On Map, click on "Validate start message"
    print("Click on Validate start message")
    mouse_click(1279, 1003)

    # On Map, click on submarine money tower
    print("Click on submarine money tower")
    mouse_click(2273, 1007)

    # On Map, click to place submarine
    print("Click to place submarine")
    mouse_click(1602, 359)

    # On Map, click on submarine money to select it
    print("Click on submarine money to select it")
    mouse_click(1602, 359)

    # On Map, Click on upgrade third path (4 times)
    print("Click on upgrade third path (4 times)")
    mouse_click(466, 1031, 4)

    # On Map, Click on upgrade first path (2 times)
    print("Click on upgrade first path (2 times)")
    mouse_click(448, 641, 2)

    # On Map, Click on center of the map to exit upgrade menu
    print("Click on center of the map to exit upgrade menu")
    mouse_click(1103, 698)

    # On Map, click on submarine money tower
    print("Click on submarine money tower")
    mouse_click(2273, 1007)

    # On Map, click to place submarine
    print("Click to place submarine")
    mouse_click(634, 1048)

    # On Map, click on submarine money to select it
    print("Click on submarine money to select it")
    mouse_click(634, 1048)

    # On Map, Click on upgrade third path (4 times)
    print("Click on upgrade third path (4 times)")
    mouse_click(2071, 1045, 4)

    # On Map, Click on upgrade first path (2 times)
    print("Click on upgrade first path (2 times)")
    mouse_click(2063, 655, 2)

    # On Map, Click on center of the map to exit upgrade menu
    print("Click on center of the map to exit upgrade menu")
    mouse_click(1103, 698)

    # On Map, scroll down on tower list
    print("Scroll down on tower list")
    mouse.position = (2431, 1011)
    time.sleep(0.1)
    mouse.scroll(0, -20)
    time.sleep(0.5)

    # On Map, click on magician money tower
    print("Click on magician money tower")
    mouse_click(2280, 642)

    # On Map, click to place magician
    print("Click to place magician")
    mouse_click(1112, 934)

    # On Map, click on magician money to select it
    print("Click on magician money to select it")
    mouse_click(1112, 934)

    # On Map, Click on upgrade third path (2 times)
    print("Click on upgrade third path (2 times)")
    mouse_click(2065, 1039, 2)

    # On Map, Click on upgrade second path (3 times)
    print("Click on upgrade second path (3 times)")
    mouse_click(2060, 856, 3)

    # On Map, Click on center of the map to exit upgrade menu
    print("Click on center of the map to exit upgrade menu")
    mouse_click(1103, 698)

    # On Map, click on magician money tower
    print("Click on magician money tower")
    mouse_click(2280, 642)

    # On Map, click to place magician
    print("Click to place magician")
    mouse_click(1112, 510)

    # On Map, click on magician money to select it
    print("Click on magician money to select it")
    mouse_click(1112, 510)

    # On Map, Click on upgrade third path (2 times)
    print("Click on upgrade third path (2 times)")
    mouse_click(2065, 1039, 2)

    # On Map, Click on upgrade second path (3 times)
    print("Click on upgrade second path (3 times)")
    mouse_click(2060, 856, 3)

    # On Map, Click on center of the map to exit upgrade menu
    print("Click on center of the map to exit upgrade menu")
    mouse_click(1103, 698)

    # On Map, click to start the game (2 times to enable fast forward)
    print("Click to start the game (2 times to enable fast forward)")
    mouse_click(2442, 1348, 2)

    # Wait for the game to finish (332 seconds)
    # time.sleep(332.0)

    for i in range(166):  # 166 = 332 / 2 (Time to click twice)
        print("Click to avoid game to pause and level up")
        mouse_click(1103, 698, 2)

    # On Map, click on "Next" button
    print("Click on Next button")
    mouse_click(1275, 1209)

    # On Map, click on "Home" button
    print("Click on Home button")
    mouse_click(928, 1119)

    main()


if __name__ == '__main__':
    main()
