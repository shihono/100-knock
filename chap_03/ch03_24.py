# -*- coding : utf-8 -*-
import re
from chap_03 import ch03_20
"""24. ファイル参照の抽出"""


def main_24():
    # 参考 : https://ja.wikipedia.org/wiki/Help:ファイルページ
    file_pattern = re.compile("\[?\[?:?(ファイル|File|Media):(?P<name>[^\|]+).*]?]?")
    data = ch03_20.main_20()
    for line in data:
        for m in file_pattern.finditer(line):
            # 1行に複数ファイルがある可能性を加味
            print(m.group('name'))


if __name__ == '__main__':
    main_24()
