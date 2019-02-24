from random import randint, choices
from itertools import product

LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
FREQUENCIES = [0.0812, 0.0149, 0.0271, 0.0432, 0.1202, 0.023, 0.0203, 0.0592, 0.0731, 0.001, 0.0069, 0.0398, 0.0261,
               0.0695, 0.0768, 0.0182, 0.0011, 0.0602, 0.0628, 0.091, 0.0288, 0.0111, 0.0209,0.0017, 0.0211, 0.0007]

class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hiddenWords = []
        self.board = [[" "  for _ in range(width)] for _ in range (height)]

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join(row) + "\n"
        return board_str

    
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
    
    def fillRandom(self):
        for i,j in product(range(self.height),range(self.width)):
            if self.board[i][j] == " ":
                self.board[i][j] = choices(population=LETTERS, weights=FREQUENCIES)[0]

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