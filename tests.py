from random import sample
from colorama import init
from time import sleep

import os
import keyboard

from models import HiddenWord, Board
from auxiliary_functions import clearConsole

init(autoreset=True, convert=True, strip=True)

with open("words.txt") as f:
    words = [x.strip() for x in f.readlines()]
    words_l = len(words) - 1


def addNWords(board, n):
    words_to_search = sample(words, n)
    for word in words_to_search:
        board.addWord(word)


def promtStartMenu(board):
    if not board:
        board = Board(1,1)
    print(board)
    clearConsole()
    print("Select difficulty:")
    print("1) Easy (10x10, 5 words)")
    print("2) Medium (15x15, 12 words)")
    print("3) Hard (20x20, 25 words)")
    print("4) Very Hard (30x30, 40 words)")
    option = 99
    while True:
        
        option = input("Your option:")
        if option == "1":
            board.__init__(10,10)
            return board, 5
        elif option == "2":
            board.__init__(15,15)
            return board, 12
        elif option == "3":
            board.__init__(20,20)
            return board, 25
        elif option == "4":
            board.__init__(30,30)
            return board, 40
        else:
            print("Please select a valid option")

# width = 10
# height = 10
# amount = 4
# board = Board(width,height)
# words_to_search = sample(words, amount)
# for word in words_to_search:
#     board.addWord(word)

board, n_words = promtStartMenu(None)
addNWords(board, n_words)
board.startGame()

def keypress(event):
    if event.event_type == "up":
        return

    if board.gameIsWon() and event.scan_code == 28:
        clearConsole()
        _, n_words = promtStartMenu(board)
        addNWords(board, n_words)
        board.startGame()

    if board.moveCursor(event.scan_code):
        board.update()
    elif event.scan_code == 28:
        board.toggleMarking()

keyboard.hook(keypress)
keyboard.wait("esc")