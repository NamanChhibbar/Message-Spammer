import random
from time import sleep
import pyautogui as pt

random.seed(0)

def spam(messages: list[str], num: int, gap: int=5):
    """
    Types and enters a random message from the given list of messages with
    specified time gap. Move mouse cursor to top left corner to stop.

    ## Parameters
    `messages`: `list` containing messages to type
    `num`: Number of messages to type
    `gap`: Time gap in seconds between messages
    """
    sleep(gap)
    for _ in range(num):
        message = random.choice(messages)
        pt.typewrite(message)
        pt.press("enter")
