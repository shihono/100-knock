# -*- coding : utf-8 -*-
import re
from itertools import dropwhile,takewhile
from chap_03 import ch03_20
"""25. テンプレートの抽出"""


def main_25():
    data = ch03_20.main_20()
    tempstart = re.compile("\{\{基礎情報")
    tempend = re.compile("\}\}")
    temp = re.compile("\|(.*)=(.*)")
    # temp=re.compile("\{\{基礎情報(.*)=(.*)\}\}")

    info_box = {}
    for t in data:
        tmatch = re.match(temp, t)
        if tmatch:
            break

    for t2 in data:
        # print(t2)
        m = re.search(temp, t2)
        if m:
            info_box[m.group(1).strip()] = m.group(2).strip()
        if re.match(tempend, t2):
            break
    return info_box


if __name__ == '__main__':
    print(main_25().items())
