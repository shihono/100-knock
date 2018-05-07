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


def main(return_value=False):
    # main
    f_t = defaultdict(int)
    f_tc = defaultdict(int)
    f_c = defaultdict(int)
    with open('./work/tuple_82.txt', 'r')as f:
        for line in f:
            t, c = line.strip().split('\t')
            f_tc[t+'\t'+c] += 1
            f_c[c] += 1
            f_t[t] += 1
    if not return_value:
        save_result_freq(f_tc, './work/ftc_83.txt')
        save_result_freq(f_t, './work/ft_83.txt')
        save_result_freq(f_c, './work/fc_83.txt')
    else:
        return f_tc, f_t, f_c


if __name__ == '__main__':
    main()