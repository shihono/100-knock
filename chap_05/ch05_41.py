# -*- coding : utf-8 -*-
from itertools import groupby
from collections import defaultdict
from chap_05 import ch05_40
"""41. 係り受け解析結果の読み込み（文節・係り受け）"""


class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = None
        self.srcs = []

    def __str__(self):
        return "dst: {}\tsrcs:{}\n{}".format(self.dst, self.srcs, '\t'.join(["{}".format(m.surface) for m in self.morphs]))

    def show_bunsetsu(self):
        """for 42: 句読点を除いた形態素の表層のリストを返す"""
        return [morph.surface for morph in self.morphs if morph.pos != "記号"]

    def show_base(self):
        return [morph.base for morph in self.morphs if morph.pos != "記号"]

    def is_contain_pos(self, pos):
        """pos の品詞が含まれているかどうか"""
        if pos in [m.pos for m in self.morphs]:
            return True
        else:
            return False


def create_each_sentence_chunk(sentence_list):
    chunk=None
    chunklist=[]
    # dependlist:係元情報を入れるlist
    dependlist=defaultdict(list)
       # 文節ごとchunkを作成
    for line in sentence_list:
        # *からはじまる場合それまでの要素を保存、新しいChunk作成
        if line.startswith("* "):
            if chunk!=None:
                chunklist.append(chunk)
            chunk=Chunk()
            chunk.dst=int(line.split()[2].strip("D"))
            # 係元情報を一旦dependlistに入れる
            if line.split()[2]!="-1D":
                srcs_point=int(line.split()[2].strip("D"))
                dependlist[srcs_point].append(int(line.split()[1].strip("D")))
        else:
            # morphを作成しchunkに追加
            el=line.rstrip().replace('\t',',').split(',')
            chunk.morphs.append(ch05_40.Morph(el[0],el[1],el[2],el[7]))
    chunklist.append(chunk)
    # 係元の情報
    for i in range(len(chunklist)):
        chunklist[i].srcs=dependlist[i]
    return chunklist


def create_chunk_list_by_cabocha():
    clist=[]
    with open('./data/neko.txt.cabocha', 'r')as f:
        for not_eos,g in groupby(f,key=lambda x:x!="EOS\n"):
            sentence_list=list(g)
            if not_eos:
                clist.append(create_each_sentence_chunk(sentence_list))
        return clist


if __name__ == '__main__':
    data = create_chunk_list_by_cabocha()
    for chunk in data[8]:
        print(chunk)