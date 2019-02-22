from random import randint


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

print(words_to_search)
    
