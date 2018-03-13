# -*- coding : utf-8 -*-
import re
from chap_03 import ch03_20
"""23. セクション構造"""


def main_23():
    sec_pattern = re.compile(r"(={2,5})(.*)\1")
    data = ch03_20.main_20()
    for line in data:
        if sec_pattern.match(line):
            sec_match = sec_pattern.match(line)
            print("{}\t{}".format(len(sec_match.group(1))-1, sec_match.group(2)))


if __name__ == '__main__':
    main_23()
