# -*- coding : utf-8 -*-
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from chap_08 import ch08_72, ch08_73
"75. 素性の重み"


def get_feature_and_predict():
    "素性抽出・学習・予測まで一括で行う"
    with open("data/sentiment.txt", 'r')as f:
        text_count_list = []
        for line in f:
            stemming_text = ch08_72.get_stemming_text(ch08_72.del_stop_words(line[2:]))
            text_count_list.append(dict(Counter(stemming_text)))
    vec = DictVectorizer(sparse=False)
    X_array = vec.fit_transform(text_count_list)

    with open("data/sentiment.txt","r")as f:
        y = [1 if line[0] == '+' else 0 for line in f]
    lr = LogisticRegression()
    lr.fit(X_array, y)
    return X_array, y,lr, vec


def main():
    X_array, _, lr, vec = get_feature_and_predict()
    feature_df = pd.DataFrame({"weight": np.absolute(lr.coef_[0]), "feature": vec.get_feature_names()})
    print(feature_df.sort_values(by="weight", ascending=False)[:10])


if __name__ == '__main__':
    main()
