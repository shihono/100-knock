# -*- coding : utf-8 -*-
import re
from itertools import islice
"""50. 文区切り"""


def get_nlp_txt():
    """文章ファイルを呼び出す関数"""
    with open("./data/nlp.txt") as f:
        for line in f:
            yield line


def main():
    pattern = "([^\.\?!:;]*[\.\?!:;])(?=(\s[A-Z])|(\n))"
    for line in get_nlp_txt():
        for m in re.finditer(pattern, line):
            yield m.group().strip()


if __name__ == '__main__':
    for line in islice(main(),10):
        print(line)