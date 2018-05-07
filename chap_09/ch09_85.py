# -*- coding : utf-8 -*-
import numpy as np
from scipy.sparse import lil_matrix
from scipy import io, sparse
from sklearn.decomposition import PCA, SparsePCA
from sklearn.decomposition import TruncatedSVD
import pandas as pd
from chap_09 import ch09_84


def main():
    # X_matrix = io.loadmat("./work/x_word_matrix_84")["xm"]
    df = ch09_84.get_freq_data()
    X_matrix = df.as_matrix()
    #pca = SparsePCA(n_components=300)
    #pca.fit(X_matrix.toarray())

    svd = TruncatedSVD(n_components=300)
    X_new = svd.fit_transform(X_matrix)
    np.save('./work/transform_85.npy',X_new)
    return pd.DataFrame(X_new, index=df.index)


if __name__ == '__main__':
    main()