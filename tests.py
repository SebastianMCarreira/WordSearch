from random import sample
from models import HiddenWord, Board
from colorama import init
from time import sleep
from os import system

import keyboard

init(autoreset=True)


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
system('cls')
print(board)

def keypress(event):
    if event.event_type == "down" and board.cursor.move(event.scan_code):
        system('cls')
        board.show()

keyboard.hook(keypress)
keyboard.wait("esc")