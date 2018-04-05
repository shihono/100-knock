# -*- coding : utf-8 -*-
from sklearn.metrics import accuracy_score
import pandas as pd
"93. アナロジータスクの正解率の計算"


def main():
    df = pd.read_table('./work/92_result_w2v.txt', sep=' ', header=None)
    print(accuracy_score(df.iloc[:, 3], df.iloc[:, 4]))


if __name__ == '__main__':
    main()