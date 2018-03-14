# -*- coding : utf-8 -*-
from itertools import groupby
from chap_04 import ch04_30
"""35. 名詞の連接"""


def main_35():
    morph_list = ch04_30.main_30()
    rensetu = []
    for row in morph_list:
        for k, g in groupby(row, lambda x: x['pos'] == "名詞"):
            meisi = list(g)
            if k and len(meisi) > 1:
                rensetu.append(''.join([m['surface'] for m in meisi]))
    return rensetu


if __name__ == '__main__':
    noun_rensetsu = main_35()
    print(noun_rensetsu[:5])
