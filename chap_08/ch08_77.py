# -*- coding : utf-8 -*-
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from chap_08 import ch08_75
"77. 正解率の計測"


def print_accuracy_f1score(y_true, y_predict):
    # 正解率、適合率、再現率、F１スコアをプリントする
    print("accuracy\t{}".format(accuracy_score(y_true,y_predict)))
    print("precision\t{}".format(precision_score(y_true,y_predict,average=None)))
    print("recall   \t{}".format(recall_score(y_true,y_predict,average=None)))
    print("f1 score\t{}".format(f1_score(y_true,y_predict,average=None)))


def main():
    X_array, y, lr, vec = ch08_75.get_feature_and_predict()
    print_accuracy_f1score(y, lr.predict(X_array))


if __name__ == '__main__':
    main()
