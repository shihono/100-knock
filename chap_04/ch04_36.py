# -*- coding : utf-8 -*-
from itertools import chain
from collections import defaultdict
from chap_04 import ch04_30
"""36. 単語の出現頻度"""


def main_36():
    morph_list = ch04_30.main_30()
    d = defaultdict(int)
    for line in chain.from_iterable(morph_list):
        word = line['surface']
        d[word] += 1
    # value で sort
    return sorted(d.items(), key=lambda x:x[1], reverse=True)


if __name__ == '__main__':
    dict_count = main_36()
    print(dict_count[:10])