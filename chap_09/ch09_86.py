# -*- coding : utf-8 -*-
import numpy as np
import pandas as pd
from chap_09 import ch09_85
"86. 単語ベクトルの表示"


def main():
    df = ch09_85.main().T
    # t_word_list = [t.strip().split()[0] for t in open('./work/ft_83.txt')]
    # X_matrix = np.load('./work/transform_85.npy')
    # print(X_matrix[t_word_list.index('United_States')])
    print(df['the'])


if __name__ == '__main__':
    main()