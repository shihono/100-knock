# -*- coding : utf-8 -*-
from chap_04 import ch04_30
"""34. 「AのB」"""


def main_34():
    morph_list = ch04_30.main_30()
    a_no_b = []
    for line in morph_list:
        for i in range(len(line) - 2):
            # 途中：lineを3-gram変換して参照したい
            if line[i]['pos'] == "名詞" \
                    and line[i + 1]['base'] == "の" \
                    and line[i + 2]['pos'] == "名詞":
                a_no_b.append(''.join(str(line[i]['surface']) + "の" + str(line[i + 2]['surface'])))
    return a_no_b


def main_34_ngram():
    # ngramを用いる場合
    from nltk.util import ngrams
    morph_list = ch04_30.main_30()
    a_no_b_ngram = []
    for line in morph_list:
        if len(line) > 3:  # 要素が３つ以上の時のみ
            for e in list(ngrams(line, 3)):
                if e[0]['pos'] == "名詞" and e[1]['base'] == "の" and e[2]['pos'] == "名詞":
                    a_no_b_ngram.append(''.join(str(e[0]['surface']) + "の" + str(e[2]['surface'])))


if __name__ == '__main__':
    rensetsu = main_34()
    print(rensetsu[:10])