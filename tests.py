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
print(board)
words_to_search = sample(words, amount)
print(words_to_search)
for word in words_to_search:
    board.addWord(word)
    print("Added: "+word)
    print(board)
    print("=======================================")

board.fillRandom()
system('cls')
print(board)

def keypress(event):
    if event.event_type == "down":
        
        moved = False
        if event.scan_code == 72:           #Move Cursor Up
            moved = board.cursor.move(0,-1)
        elif event.scan_code == 77:         #Move Cursor Right
            moved = board.cursor.move(1,0)
        elif event.scan_code == 80:         #Move Cursor Down
            moved = board.cursor.move(0,1)
        elif event.scan_code == 75:         #Move Cursor Left
            moved = board.cursor.move(-1,0)
        
        if moved:
            system('cls')
            board.show()

        

keyboard.hook(keypress)
keyboard.wait("esc")