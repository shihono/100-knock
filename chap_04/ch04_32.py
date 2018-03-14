# -*- coding : utf-8 -*-
from itertools import chain
from chap_04 import ch04_30
"""32. 動詞の原形"""


def main_32():
    morph_list = ch04_30.main_30()
    return [line['base'] for line in chain.from_iterable(morph_list) if line['pos'] == '動詞']


if __name__ == '__main__':
    verb = main_32()
    print(verb[:10])