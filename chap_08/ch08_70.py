# -*- coding : utf-8 -*-
from collections import Counter
import random
import pprint
"70. データの入手・整形"


def add_label(label:str, data_path:str):
    with open(data_path, 'r', encoding="cp1251")as f:
        labeled_data = [label + ' ' + line.strip() for line in f]
    return labeled_data


def main():
    # それぞれ読み込んで文字列を追加する
    plus_label = add_label('+1', "data/rt-polaritydata/rt-polarity.pos")
    print("plus:{}".format(len(plus_label)))

    minus_label = add_label("-1", "data/rt-polaritydata/rt-polarity.neg")
    print("minus:{}".format(len(minus_label)))

    # シャッフルする
    label_set = plus_label + minus_label
    random.shuffle(label_set)
    with open("data/sentiment.txt",'w')as f:
        f.write("\n".join(label_set))

    # 正例負例の確認
    with open("data/sentiment.txt", 'r')as f:
        polarity_counter = Counter([line[0] for line in f])
    pprint.pprint(polarity_counter)


if __name__ == '__main__':
    main()