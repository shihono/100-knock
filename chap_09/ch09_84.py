# -*- coding : utf-8 -*-
from collections import defaultdict
from scipy.sparse import lil_matrix
from scipy import io, sparse
import math
from tqdm import tqdm
"84. 単語文脈行列の作成"


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
    main()