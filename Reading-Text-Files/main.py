# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count
from operator import index
from nbformat import read
from collections import Counter


def read_file_content(filename):
    with open('story.txt','r') as f:
        file = f.read() 
    return file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.split()
    return words

val = count_words()
print(Counter(val))
