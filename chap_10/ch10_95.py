# -*- coding : utf-8 -*-
import pandas as pd
from scipy.stats import spearmanr


def main():
    df = pd.read_csv('./work/94_w2v.csv', names=['word1', 'word2', 'human', 'w2v_cos'])
    print(spearmanr(df['human'], df['w2v_cos']))


if __name__ == '__main__':
    main()