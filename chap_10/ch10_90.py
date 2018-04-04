# -*- coding : utf-8 -*-
import os
import gensim
from gensim.models import word2vec, KeyedVectors
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
WORD_VECTOR_FILE = './work/vector90_small.txt'
"90. word2vecによる学習"


def main(text_data_path):
    if os.path.exists(WORD_VECTOR_FILE):
        word_vectors = KeyedVectors.load_word2vec_format(WORD_VECTOR_FILE)
    else:
        sentences = word2vec.LineSentence(text_data_path)
        model = gensim.models.Word2Vec(sentences)
        model.wv.save_word2vec_format('./work/vector90_small.txt')
        word_vectors = model.wv
        del model
    print("#86 United Statesのベクトルを表示\n {}".format(word_vectors['United_States']))
    print("# 87 United StatesとU.S.のコサイン類似度を計算せよ {}".format(word_vectors.similarity('United_States', 'U.S')))
    print("""# 88 "England"とコサイン類似度が高い10語と，その類似度を出力せよ""")
    for item in word_vectors.most_similar('England'):
        print(item)
    print("""# vec("Spain") - vec("Madrid") + vec("Athens")を計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ""")
    for item in word_vectors.most_similar_cosmul(positive=['Spain', 'Madrid'], negative=['Athens']):
        print(item)


if __name__ == '__main__':
    # 勉強会で生成したファイルを使用
    main('/Users/shirai/100knock-2017/shihono/sh_chap09/data/small/enwiki-81.txt')