# -*- coding : utf-8 -*-
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from itertools import islice
from chap_10 import ch10_97
"99. t-SNEによる可視化"

def main():
    X_array, y = ch10_97.get_clustering_data()
    km = KMeans(n_clusters=5, random_state=1)
    kmeans_pred = km.fit_predict(X_array)
    X_reduced = TSNE(n_components=2, random_state=0).fit_transform(X_array)

    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=kmeans_pred)
    for idx, name in enumerate(y):
        # 名前の表示
        plt.plot(X_reduced[idx, 0], X_reduced[idx, 1], marker="${}$".format(name), markersize=20, c='black', alpha=0.7)
    plt.plot()
    plt.show()


if __name__ == '__main__':
    main()