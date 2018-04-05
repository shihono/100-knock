# -*- coding : utf-8 -*-
import gensim
from gensim.models import word2vec, KeyedVectors
from chap_10 import ch10_90
"92. アナロジーデータへの適用"


def main(wv, save_path):
    with open(save_path, 'w')as fw:
        with open("./work/91_analogy.txt", 'r') as fr:
            for line in fr:
                col1, col2, col3 = line.strip().split()[:3]
                try:
                    # wip keyerror
                    vec = wv.most_similar(positive=[col2, col3], negative=[col1],topn=1)[0]
                    fw.write("{} {} {}\n".format(line.strip(), vec[0], vec[1]))
                except(KeyError):
                    fw.write("{} {} {}\n".format(line.strip(), None, 0))


if __name__ == '__main__':
    word_vector = ch10_90.load_w2v_data()
    main(word_vector, './work/92_result_w2v.txt')