# -*- coding : utf-8 -*-
from itertools import islice
from chap_06 import ch06_50
"""51. 単語の切り出し"""


def cut_words(sentence:str):
    split_words = sentence.split(" ")
    for word in split_words:
        yield word
    yield "\n"


def main():
    for sent in ch06_50.main():
        word_list = list(cut_words(sent))
        yield word_list


if __name__ == '__main__':
    for line in islice(main(),10):
        print(line)