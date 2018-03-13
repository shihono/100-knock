# -*- coding : utf-8 -*-
import re
from chap_03 import ch03_20
"""21. カテゴリ名を含む行を抽出"""


def main_21():
    # "[[ Category:" + ＊　+ "]]"
    pattern = re.compile("\[\[Category:.*]]")
    data = ch03_20.main_20()
    for line in data:
        if pattern.match(line):
            print(line)


if __name__ == '__main__':
    main_21()