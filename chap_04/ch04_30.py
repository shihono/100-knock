# -*- coding : utf-8 -*-
from itertools import groupby
"""30. 形態素解析結果の読み込み"""


def main_30():
    """
    input : 「表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音」
    return : morph = [[{base:＊ pos:＊}, {}, {}, ...][{}...]....[...{}]]
    """
    with open('./data/neko.txt.mecab', 'r')as f:
        morph = []
        for is_eos, value in groupby(f, key=lambda x: x.strip() != "EOS"):
            value_list = list(value)
            if is_eos:
                sentence = []
                for line in value_list:
                    surface, feature = line.strip().split('\t')
                    result = {m: feature.split(',')[n] for n, m in zip([0, 1, 6], ["pos", "pos1", "base"])}
                    result["surface"]=surface
                    sentence.append(result)
                morph.append(sentence)
        return morph


if __name__ == '__main__':
    morph = main_30()
    print(morph[:5])