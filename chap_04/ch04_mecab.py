# -*- coding : utf-8 -*-
from natto import MeCab
"""形態素解析をして　neko.txt.mecabに保存"""
save_path= './data/neko.txt.mecab'


def main_mecab():
    mc = MeCab()
    with open('./data/neko.txt', 'r')as f:
        with open(save_path,'w')as fw:
            for line in f:
                for one_sent in line.strip().split():
                    # １行に2 sentence 以上ある場合
                    fw.write(mc.parse(one_sent.strip())+"\n")
    print("save mecab file {}".format(save_path))


if __name__ == '__main__':
    main_mecab()
