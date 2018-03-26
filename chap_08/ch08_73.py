# -*- coding : utf-8 -*-
from sklearn.linear_model import LogisticRegression
from chap_08 import ch08_72
"73. 学習"


def main(X_array=None):
    if X_array is None:
        X_array = ch08_72.main()
    with open("data/sentiment.txt","r")as f:
        y = [1 if line[0] == '+' else 0 for line in f]
    lr = LogisticRegression()
    lr.fit(X_array, y)
    return lr


if __name__ == '__main__':
    main()