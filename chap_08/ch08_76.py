# -*- coding : utf-8 -*-
import numpy as np
import pandas as pd
from chap_08 import ch08_75


def main():
    X_array, y, lr, vec = ch08_75.get_feature_and_predict()
    labels = np.array([np.array(y), lr.predict(X_array)])
    # タブ区切りで出力
    np.savetxt("data/76.txt", np.hstack((labels.T, lr.predict_proba(X_array))), delimiter="\t")
    plus_predict, minus_predict = lr.predict_proba(X_array).T
    result = pd.DataFrame(list(zip(y, lr.predict(X_array), plus_predict, minus_predict)),
                          columns=["true", "pred", "plus", "minus"])
    return result


if __name__ == '__main__':
    main()