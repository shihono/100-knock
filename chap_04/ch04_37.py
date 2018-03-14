# -*- coding : utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from chap_04 import ch04_36

"""37. 頻度上位10語"""


def main_37():
    freq_list = ch04_36.main_36()
    # plt.rcParams['font.family'] = 'IPAPGothic'
    x_tick = [i for i in range(10)]
    plt.bar(x_tick, [line[1] for line in freq_list[:10]])
    # 日本語設定をしてる場合
    # plt.xticks(x_tick, [line[0] for line in freq_list[:10]])
    plt.ylabel('frequency')
    plt.show()


if __name__ == '__main__':
    main_37()
