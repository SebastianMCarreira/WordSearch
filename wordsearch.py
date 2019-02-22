from random import randint

class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hiddenWords = []
        self.board = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(" ")
            self.board.append(row)

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join(row) + "\n"
        return board_str

    
    def addWord(self, word):
        if (word.x1 in range(0, self.width-1) and word.x2 in range(0, self.width-1) and 
            word.y1 in range(0, self.height-1) and word.y2 in range(0, self.height-1)):
            if word.vert:
                for i, letter in enumerate(word.word):
                   self.board[word.y1+i][word.x1] = letter
            else:
                for i, letter in enumerate(word.word):
                    self.board[word.y1][word.x1+i] = letter
        else:
            raise ValueError("The word does not fit with the specified coordinates ({},{}) and length {}".format(
                                                                                word.x1,word.y1,len(word.word)))



class HiddenWord():
    def __init__(self, word, x1, y1, vert):
        self.vert = vert

        self.word = word
        self.letters = list(set(word))

        self.x1 = x1
        self.y1 = y1
        if vert:
            self.x2 = x1
            self.y2 = y1 + len(word)
        else:
            self.y2 = y1
            self.x2 = x1 + len(word)

        



with open("words.txt") as f:
    words = [x.strip() for x in f.readlines()]
    words_l = len(words) - 1

width = 15
height = 15
amount = 7


words_to_search = []
for x in range(amount):
    search = True
    while search:
        new_word = words[randint(0,words_l)]
        if new_word not in words_to_search:
            search = False
    words_to_search.append(new_word)

for word in words_to_search:
    if randint(0,1):
        vert = True
    else:
        vert = False

    
board = Board(width,height)
board.addWord(HiddenWord("putostotods",10,4,False))
print(board)