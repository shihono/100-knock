# -*- coding : utf-8 -*-
from collections import Counter
from stemming.porter2 import stem
from sklearn.feature_extraction import DictVectorizer
from chap_08 import ch08_71
"72. 素性抽出"


def del_stop_words(text: str):
    text_list = text.strip().split()
    return [word for word in text_list if not ch08_71.is_contain_stop_word(word)]

# ステミング処理
def get_stemming_text(text_list: list):
    return [stem(word) for word in text_list]


def main():
    with open("data/sentiment.txt", 'r')as f:
        file = f.readlines()
    text_count_list = []
    for line in file:
        stemming_text = get_stemming_text(del_stop_words(line[2:]))
        text_count_list.append(dict(Counter(stemming_text)))
    # vectorizer
    # とりあえずベースラインで
    vec = DictVectorizer(sparse=False)
    X_array = vec.fit_transform(text_count_list)
    return X_array


if __name__ == '__main__':
    main()
