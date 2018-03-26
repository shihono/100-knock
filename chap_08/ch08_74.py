# -*- coding : utf-8 -*-
from chap_08 import ch08_72, ch08_73


def main():
    X_array = ch08_72.main()
    lr = ch08_73.main(X_array)
    print(lr.predict_proba(X_array[:10]))


if __name__ == '__main__':
    main()