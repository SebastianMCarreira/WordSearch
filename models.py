from random import randint, choices
from itertools import product
from colorama import Back, Fore

import os

if os.name == "nt":
    from ctypes import windll, c_short, c_char_p, Structure

LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
FREQUENCIES = [0.0812, 0.0149, 0.0271, 0.0432, 0.1202, 0.023, 0.0203, 0.0592, 0.0731, 0.001, 0.0069, 0.0398, 0.0261,
               0.0695, 0.0768, 0.0182, 0.0011, 0.0602, 0.0628, 0.091, 0.0288, 0.0111, 0.0209,0.0017, 0.0211, 0.0007]

def moveConsoleCursor(x,y):
    if os.name == "nt":
        STD_OUTPUT_HANDLE = -11
 
        class COORD(Structure):
            pass
        COORD._fields_ = [("X", c_short), ("Y", c_short)]

        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(h, COORD(x, y))
    else:
        print('\033[{};{}H'.format(str(x+1),str(y+1))) 

class Cursor():
    def __init__(self, limit_x, limit_y):
        self.x = 0
        self.y = 0
        self.lastX = 0
        self.lastY = 0
        self.limit_x = limit_x
        self.limit_y = limit_y

    def move(self, code): #Returns True if the cursor moved
        self.lastX = self.x
        self.lastY = self.y
        if code == 75 and self.x != 0:
            self.x -= 1
            return True
        elif code == 77 and self.x != self.limit_x:
            self.x += 1
            return True
        elif code == 72 and self.y != 0:
            self.y -= 1
            return True
        elif code == 80 and self.y != self.limit_y:
            self.y += 1
            return True

        return False


class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hiddenWords = []
        self.board = [[" "  for _ in range(width)] for _ in range (height)]
        self.cursor = Cursor(width - 1, height - 1)

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join(row) + "\n"
        return board_str

    def show(self):
        for j,i in product(range(self.height),range(self.width)):

            # if i == self.cursor.lastX and j == self.cursor.lastY:
            #     print(self.board[j][i], end=" ")
            if i == self.cursor.x and j == self.cursor.y:
                print(Fore.RED + self.board[j][i], end=" ")
            else:
                print(self.board[j][i], end=" ")
            
            if i == self.width - 1:
                print("")

    def update(self):
        moveConsoleCursor(self.cursor.lastX*2,self.cursor.lastY)
        print(self.board[self.cursor.lastY][self.cursor.lastX], end=" ")
        moveConsoleCursor(self.cursor.x*2,self.cursor.y)
        print(Fore.RED + self.board[self.cursor.y][self.cursor.x], end=" ")
        moveConsoleCursor(self.cursor.x*2,self.cursor.y)
    
    def addWord(self, word):
        length = len(word)
        hidWord = HiddenWord(word,self.width-length,self.height-length)


        ## TODO: Reformat this mess.s
        ## TODO: If the board is too small, there is a chance that it will not be able to place a word and get
        ##       stuck in a loop trying to reroll the coordinates until it can be placed.
        isInOccupiedSpaces = True
        while isInOccupiedSpaces:
            foundOneOccupied = False
            for coord, letter in zip(hidWord.spaces, hidWord.word):
                if self.board[coord[1]][coord[0]] != letter and self.board[coord[1]][coord[0]] != " ":
                    hidWord.rerollCoordinates(self.width-length,self.height-length)
                    foundOneOccupied = True
            isInOccupiedSpaces = foundOneOccupied
        for coord, letter in zip(hidWord.spaces, hidWord.word):
            self.board[coord[1]][coord[0]] = letter
        self.hiddenWords.append(hidWord)
    
    def fillRandom(self):
        for i,j in product(range(self.height),range(self.width)):
            if self.board[i][j] == " ":
                self.board[i][j] = choices(population=LETTERS, weights=FREQUENCIES)[0]

    def showWords(self):
        moveConsoleCursor(0,self.height)
        print("==============================")
        print("Words to search:")
        for word in self.hiddenWords:
            print("- " + word.word)

        

class HiddenWord():
    def __init__(self, word, limit_x, limit_y):
        self.vert = bool(randint(0,1)) # True if the word is vertical, False if horizontal, diagonals for the future

        self.word = word # The actual word to search
        # self.letters = list(set(word))

        self.spaces = [(randint(0,limit_x),randint(0,limit_y))]
        self.calculateSpaces(limit_x, limit_y)
 
    def calculateSpaces(self, x, y):
        for _ in self.word:
            lastCoord = self.spaces[-1]
            if self.vert:
                self.spaces.append((lastCoord[0],lastCoord[1]+1))
            else:
                self.spaces.append((lastCoord[0]+1,lastCoord[1]))

    def rerollCoordinates(self, limit_x, limit_y):
        self.spaces = [(randint(0,limit_x),randint(0,limit_y))]
        self.calculateSpaces(limit_x, limit_y)