from random import sample
from models import HiddenWord, Board

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
print(board)