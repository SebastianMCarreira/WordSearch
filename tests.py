from random import sample
from models import HiddenWord, Board
from colorama import init
from time import sleep

import os
import keyboard

init(autoreset=True, convert=True, strip=True)

if os.name == "nt":
    from ctypes import windll, c_short, c_char_p, Structure


with open("words.txt") as f:
    words = [x.strip() for x in f.readlines()]
    words_l = len(words) - 1

width = 15
height = 15
amount = 7
board = Board(width,height)
words_to_search = sample(words, amount)
for word in words_to_search:
    board.addWord(word)

board.fillRandom()
os.system('cls')
board.show()
board.showWords()

def keypress(event):
    if event.event_type == "up":
        return
    if board.moveCursor(event.scan_code):
        board.update()
    elif event.scan_code == 28:
        board.toggleMarking()

keyboard.hook(keypress)
keyboard.wait("esc")