# -*- coding : utf-8 -*-
from itertools import groupby
"""40. 係り受け解析結果の読み込み（形態素）"""


class Morph:
    """形態素を表すクラス"""
    def __init__(self, surface, pos, pos1, base):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return ',\t'.join([self.surface, self.base, self.pos, self.pos1])


class MorphSent():
    """形態素Moprhクラスのリスト"""
    def __init__(self, g_value):
        self.morphs = []
        self.make_morph_sentence_list(sent_list=g_value)

    def __str__(self):
        return '\n'.join(["{}".format(m) for m in self.morphs])

    def make_morph_sentence_list(self, sent_list):
        for sent in sent_list:
            elements = sent.rstrip().replace('\t', ',', 1).split(',')
            if len(elements) > 1:
                self.morphs.append(Morph(elements[0], elements[1], elements[2], elements[7]))


def main():
    morph_list = []
    with open('./data/neko.txt.cabocha', 'r')as f:
        for not_eos , value in groupby(f, key=lambda x: x.strip() != "EOS"):
            group_value = list(value)
            if not_eos and len(group_value)>1:
                # 一文ごとに MorphSentを作成
                sent_morph_list=MorphSent(group_value)
                morph_list.append(sent_morph_list)
    return morph_list


if __name__ == '__main__':
    morphs = main()
    print(morphs[3])