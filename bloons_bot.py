#!/usr/bin/env python

import time
import json
import argparse

from bot import mouse_click, mouse_scroll

def main():
    parser = argparse.ArgumentParser(description='Bloons TD 6 Bot')
    parser.add_argument('--config', type=str, default='bloons_bot.json', help='Path to config file')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    args = parser.parse_args()

    data = None
    time.sleep(4.0)
    with open("bloons_bot_short.json", "r") as f:
        data = json.load(f)

    for i, action in enumerate(data['actions']):
        print("Information: {}".format(action.get("information")))
        print("Name: {}".format(action.get("name")))
        print("Type: {}".format(action.get("type")))

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
        print()

    # with open("bloons_bot.json", "w") as f:
    #     json.dump(data, f, indent=4)

    # main()


if __name__ == "__main__":
    main()
