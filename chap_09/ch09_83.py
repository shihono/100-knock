# -*- coding : utf-8 -*-
from collections import defaultdict
from scipy.sparse import lil_matrix
from scipy import io, sparse
import math
from tqdm import tqdm

"""
83. 単語／文脈の頻度の計測
f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数
"""


def save_result_freq(freq_dic, data_path):
    with open(data_path, 'w')as f:
        for k,v in freq_dic.items():
            f.write("{}\t{}\n".format(k,v))
    print("save {}".format(data_path))


def main():
    # main
    f_t = defaultdict(lambda: len(f_t))
    f_tc = defaultdict(lambda: len(f_tc))
    f_c = defaultdict(lambda : len(f_c))
    with open('./work/tuple_82.txt', 'r')as f:
        for line in f:
            f_tc[line.strip()]
            t, c = line.strip().split('\t')
            f_c[c]
            f_t[t]
    save_result_freq(f_tc, './work/ftc_83.txt')
    save_result_freq(f_t, './work/ft_83.txt')
    save_result_freq(f_c, './work/fc_83.txt')
    # 分布出力


if __name__ == '__main__':
    main()