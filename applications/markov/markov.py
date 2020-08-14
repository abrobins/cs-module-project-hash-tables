import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split(" ")


def create_wordindex(words):
    word_index = {}
    for i in range(len(words) - 1):
        if words[i] in word_index:
            word_index[words[i]].append(words[i+1])
        else:
            word_index[words[i]] = []
            word_index[words[i]].append(words[i+1])
    return word_index

# TODO: construct 5 random sentences
# Your code here


word_index = create_wordindex(words)
sample = random.choice(words)
print(" ".join(word_index[sample]), end=" ")
