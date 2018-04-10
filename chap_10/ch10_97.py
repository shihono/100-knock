# -*- coding : utf-8 -*-
from sklearn.cluster import KMeans
import numpy as np
from chap_10 import ch10_96
"97. k-meansクラスタリング"


def get_clustering_data():
    country_vec = ch10_96.main(is_return=True)
    X_array = [np.array(v) for _, v in sorted(country_vec.items(),key=lambda x:x[0])]
    y= sorted(country_vec.keys())
    return X_array, y


def main():
    X_array, y = get_clustering_data()
    km = KMeans(n_clusters=5, random_state=1)
    kmeans_pred = km.fit_predict(X_array)
    for k,v in zip(y, kmeans_pred):
        print("{} : {}".format(k,v))


if __name__ == '__main__':
    main()