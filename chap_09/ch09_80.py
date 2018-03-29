# -*- coding : utf-8 -*-
from itertools import islice
import bz2
"""
80. コーパスの整形
1/100サンプリングのコーパスenwiki-20150112-400-r100-10576.txt.bz2を用いる
"""
remove_strings= """.,!?;:()[]\'\""""


def shaping_corpus(corpus_data_path):
    with bz2.open(corpus_data_path, 'rt') as f:
        for line in f:
            line_list = line.strip().split()
            tokens = filter(lambda tok: len(tok) != ' ', [token.strip(remove_strings) for token in line_list])
            # 1 sentenceのtokenをスペース区切りで返す
            yield " ".join(tokens)


def main():
    # main
    with open('./data/enwiki-80.txt', 'w')as f:
        # /Users/shirai/100knock-2017/shihono/sh_chap09/data/enwiki-20150112-400-r100-105752.txt.bz2
        for tokens in islice(shaping_corpus('./data/enwiki-20150112-400-r100-105752.txt.bz2'),10):
            f.write(tokens + "\n")


if __name__ == '__main__':
    main()