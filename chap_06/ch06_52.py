# -*- coding : utf-8 -*-
from stemming.porter2 import stem
import pprint
from chap_06 import ch06_51
"""52. ステミング"""


def steming_word(word:str):
    return "{} \t {}".format(word,stem(word))


def main():
    sentence_word_list = [list(line) for line in ch06_51.main()]
    for word in sentence_word_list[3]:
        pprint.pprint(steming_word(word))


if __name__ == '__main__':
    main()