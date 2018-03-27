# -*- coding : utf-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
from sklearn.feature_extraction import DictVectorizer
import matplotlib.pyplot as plt
from chap_08 import ch08_78
"79. 適合率-再現率グラフの描画"


def main():
    X_text,y = ch08_78.make_x_y_text()
    vec = DictVectorizer(sparse=False)
    X_array = vec.fit_transform(X_text)
    X_train, X_test, y_train, y_test = train_test_split(X_array, y, test_size=0.2)
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    y_score = lr.decision_function(X_test)
    average_precision = average_precision_score(y_test, y_score)
    precision, recall, _ = precision_recall_curve(y_test, y_score)

    # グラフ設定
    plt.step(recall, precision, color='b', alpha=0.2, where='post')
    plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('2-class Precision-Recall curve: AUC={0:0.2f}'.format(average_precision))
    plt.show()


if __name__ == '__main__':
    main()
