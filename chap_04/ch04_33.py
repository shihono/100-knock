# -*- coding : utf-8 -*-
from itertools import chain
from chap_04 import ch04_30
"""33. サ変名詞"""


def main_33():
    morph_list = ch04_30.main_30()
    return [line['base'] for line in chain.from_iterable(morph_list) if line['pos1']=='サ変接続' and line['pos']=="名詞"]


if __name__ == '__main__':
    nouns = main_33()
    print(nouns[:10])