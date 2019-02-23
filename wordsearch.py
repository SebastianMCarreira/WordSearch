from random import randint, sample

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
        for coord, letter in zip(hidWord.spaces, hidWord.word):
            self.board[coord[1]][coord[0]] = letter



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
    added = True
    while added:
        try:
            board.addWord(word)
            added = False
            print("Added: "+word)
            print(board)
            print("=======================================")
        except ValueError:
            pass