# -*- coding : utf-8 -*-
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt
from chap_10 import ch10_97
"98. Ward法によるクラスタリング"


def main():
    X_array, y = ch10_97.get_clustering_data()
    z = linkage(X_array, method='ward')
    plt.figure(figsize=(40, 25))
    dendrogram(z,
               color_threshold=5.,
               above_threshold_color='black',
               p=100, truncate_mode='lastp',
               labels=y)
    plt.plot()
    plt.show()


if __name__ == '__main__':
    main()