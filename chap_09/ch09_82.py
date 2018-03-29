# -*- coding : utf-8 -*-
import numpy as np
from tqdm import tqdm
"""82. 文脈の抽出"""
np.random.seed(1)


def extract_context_pair(one_sentence):
    word_list = one_sentence.strip().split()
    pair_list = []
    for idx in range(len(word_list)):
        window_size = np.random.randint(1, 5)
        pair_list.extend(["{}\t{}".format(word_list[idx], dw) for dw
                          in word_list[max(0, idx - window_size):idx] + word_list[idx + 1:min(idx + window_size,
                                                                                              len(word_list))]])
    return pair_list


def main():
    # main
    with open('./work/tuple_82.txt', 'w')as fw:
        with open('./data/enwiki-81.txt', 'r')as f:
            for line in tqdm(f):
                for pair in extract_context_pair(line):
                    fw.write(pair + "\n")


if __name__ == '__main__':
    main()