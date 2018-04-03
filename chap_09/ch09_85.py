# -*- coding : utf-8 -*-
import numpy as np
from scipy.sparse import lil_matrix
from scipy import io, sparse
from sklearn.decomposition import PCA, SparsePCA
from sklearn.decomposition import TruncatedSVD


def main():
    X_matrix = io.loadmat("./work/x_word_matrix_84")["xm"]
    pca = SparsePCA(n_components=300)
    pca.fit(X_matrix.toarray())

    #svd = TruncatedSVD(n_components=300)
    #X_new = svd.fit_transform(X_matrix)
    np.save('./work/transform_85.npy',X_matrix)


if __name__ == '__main__':
    main()