# -*- coding : utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from chap_04 import ch04_36

"""38. ヒストグラム"""


def main_38():
    freq_list = ch04_36.main_36()
    plt.hist(list(Counter([line[1] for line in freq_list])), bins=20)
    plt.xlabel("frequency")
    plt.ylabel("kind of words")
    plt.show()


if __name__ == '__main__':
    main_38()
