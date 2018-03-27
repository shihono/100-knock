# -*- coding : utf-8 -*-
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from collections import Counter
from chap_08 import ch08_72, ch08_77
"78. 5分割交差検定"


def make_x_y_text():
    # データ作成
    X_text = []
    y_text = []
    with open("data/sentiment.txt", 'r')as f:
        for line in f:
            stemming_text = ch08_72.get_stemming_text(ch08_72.del_stop_words(line[2:]))
            X_text.append(dict(Counter(stemming_text)))
            if line[0] == '+':
                y_text.append(1)
            else:
                y_text.append(0)
    return X_text, y_text


def main():
    X_text, y_text = make_x_y_text()
    # K-hold
    kf = KFold(n_splits=5)
    kf.get_n_splits(X_text, y_text)
    for train_idx, test_idx in kf.split(X_text, y_text):
        lr = LogisticRegression()
        X_train, y_train = [X_text[idx] for idx in train_idx], [y_text[idx] for idx in train_idx]
        X_test, y_test = [X_text[idx] for idx in test_idx], [y_text[idx] for idx in test_idx]
        vec = DictVectorizer(sparse=False)
        X_train_vec = vec.fit_transform(X_train)
        X_test_vec = vec.transform(X_test)
        lr.fit(X_train_vec, y_train)
        ch08_77.print_accuracy_f1score(y_test, lr.predict(X_test_vec))
        print("***")


if __name__ == '__main__':
    main()