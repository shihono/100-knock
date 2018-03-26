# -*- coding : utf-8 -*-
# http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
"71. ストップワード"


def is_contain_stop_word(word:str, stop_word_list=ENGLISH_STOP_WORDS):
    return word in set(stop_word_list)


def test_is_contain_stop_word():
    assert is_contain_stop_word("is")
    assert is_contain_stop_word("was")
    assert not is_contain_stop_word("dog")


if __name__ == '__main__':
    test_is_contain_stop_word()
