# -*- coding : utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from chap_04 import ch04_36

"""39. Zipfの法則"""


def main_39():
    # 単語の出現頻度順位を横軸，その出現頻度を縦軸
    # freq_list はsort済みなので順位とindexが一致している
    freq_list = ch04_36.main_36()
    s = pd.Series([f[1] for f in freq_list])
    s.plot(loglog=True)
    plt.show()


if __name__ == '__main__':
    main_39()
