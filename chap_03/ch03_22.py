# -*- coding : utf-8 -*-
import re
from chap_03 import ch03_20
"""22. カテゴリ名の抽出"""


def main_22():
    # groupを使う
    pattern = re.compile("\[\[Category:(.*)]]")
    data = ch03_20.main_20()
    for line in data:
        if pattern.match(line):
            print(pattern.match(line).group(1))


if __name__ == '__main__':
    main_22()