from random import sample
from colorama import init
from time import sleep

import os
import keyboard

from models import HiddenWord, Board
from auxiliary_functions import clearConsole, moveConsoleCursor

init(autoreset=True, convert=True, strip=True)

IN_MENU = True
OPTION = 1

with open("words.txt") as f:
    words = [x.strip() for x in f.readlines()]
    words_l = len(words) - 1

def promtStartMenu():
    board = Board(1,1)
    print(board)
    clearConsole()
    print("Select difficulty:")
    print("> Easy (10x10, 5 words)")
    print("  Medium (15x15, 12 words)")
    print("  Hard (20x20, 25 words)")
    print("  Very Hard (30x30, 40 words)")
    IN_MENU = True
    OPTION = 1

# width = 10
# height = 10
# amount = 4
# board = Board(width,height)
# words_to_search = sample(words, amount)
# for word in words_to_search:
#     board.addWord(word)

promtStartMenu()
board = None

def keypress(event):
    global OPTION
    global IN_MENU
    global board

    if event.event_type == "up":
        return

    if IN_MENU:
        if event.scan_code == 72 and OPTION > 1:
            moveConsoleCursor(0,OPTION)
            print(" ",end="")
            OPTION -= 1
            moveConsoleCursor(0,OPTION)
            print(">",end="")
        elif event.scan_code == 80 and OPTION < 4:
            moveConsoleCursor(0,OPTION)
            print(" ",end="")
            OPTION += 1
            moveConsoleCursor(0,OPTION)
            print(">",end="")
        elif event.scan_code == 28:
            if OPTION == 1:
                board = Board(10,10)
                n_words = 5
            elif OPTION == 2:
                board = Board(15,15)
                n_words = 12
            elif OPTION == 3:
                board = Board(20,20)
                n_words = 25
            elif OPTION == 4:
                board = Board(30,30)
                n_words = 40
            else:
                raise ValueError("Option variable is out of bounds: "+str(OPTION))
            
            words_to_search = sample(words, n_words)
            for word in words_to_search:
                board.addWord(word)
            IN_MENU = False
            board.startGame()

    else:
        if board.gameIsWon():
            if event.scan_code == 28:
                IN_MENU = True
                OPTION = 1
                promtStartMenu()
                return
        else:
            if board.moveCursor(event.scan_code):
                board.update()
            elif event.scan_code == 28:
                board.toggleMarking()

keyboard.hook(keypress)
keyboard.wait("esc")