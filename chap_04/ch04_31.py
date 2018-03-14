# -*- coding : utf-8 -*-
from itertools import chain
from chap_04 import ch04_30
"""31. 動詞"""


def main_31():
    morph_list = ch04_30.main_30()
    return [line['surface'] for line in chain.from_iterable(morph_list) if line['pos'] == '動詞']


if __name__ == '__main__':
    verbs = main_31()
    print(verbs[:10])