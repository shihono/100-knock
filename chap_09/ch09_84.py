# -*- coding : utf-8 -*-
from collections import defaultdict
from scipy.sparse import lil_matrix
from scipy import io, sparse
import math
from tqdm import tqdm
import pandas as pd
from chap_09 import ch09_83
"84. 単語文脈行列の作成"


def get_freq_data():
    # 83の結果を用いて文脈を計算する
    f_tc, f_t, f_c = ch09_83.main(return_value=True)
    word_id_t = defaultdict(lambda: len(word_id_t))
    word_id_c = defaultdict(lambda: len(word_id_c))
    for key_word in f_t.keys():
        word_id_t[key_word]
    for key_word in f_c.keys():
        word_id_c[key_word]
    n = sum(f_tc.values())
    word_matrix = lil_matrix((len(f_t), len(f_c)))
    for tc, cnt in f_tc.items():
        if cnt >= 10:
            t, c = tc.strip().split('\t')
            word_matrix[word_id_t[t], word_id_c[c]] = max(math.log(n*cnt / f_t[t] * f_c[c]), 0)
    word_matrix.toarray()
    df = pd.DataFrame(word_matrix.toarray(),
                      columns=[word[0] for word in sorted(word_id_t.items(), key=lambda x: x[1])],
                      index=[word[0] for word in sorted(word_id_c.items(), key=lambda x: x[1])])
    return df


def main():
    # main
    word_id = defaultdict(lambda: len(word_id))

    with open('./work/tuple_82.txt', 'r')as f:

        for line in f:
            t, c = line.strip().split('\t')
            word_id[t]
            word_id[c]
        word_matrix = lil_matrix((len(word_id), len(word_id)))
        for line in f:
            t, c = line.strip().split('\t')
            word_matrix[word_id[t], word_id[c]] += 1
    row_idxs, col_idxs = word_matrix.nonzero()
    X_matrix = lil_matrix((len(word_id), len(word_id)))
    log_n = math.log(len(word_id))
    print(len(row_idxs), len(word_id), log_n)

    wm_csr = word_matrix.tocsr()
    wm_csc = word_matrix.tocsc()
    for row, col in tqdm(zip(row_idxs, col_idxs)):
        if word_matrix[row, col] >= 10:
            X_matrix[row, col] = max(
                log_n * word_matrix[row, col] / (wm_csr.getrow(row).sum() * wm_csc.getcol(col).sum()), 0)
    io.savemat("./work/x_word_matrix_84", {"xm": X_matrix})


if __name__ == '__main__':
    # main()
    get_freq_data()