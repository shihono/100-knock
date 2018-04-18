# -*- coding : utf-8 -*-
from lxml import etree
import regex
import re
"59. S式の解析"


def get_np(text):
    # 括弧の数を合わせる、括弧が閉じる場所までのテキスト取得(NP ...)
    paren = 0
    for idx, word in enumerate(text):
        if paren == -1:
            return text[:idx-1]
        elif word == '(':
            paren += 1
        elif word == ')':
            paren -= 1
    return None


def find_np_recursive(text, pattern):
    # 入れ子構造を考えるように再帰を用いる
    for find_pattern in re.finditer(pattern, text):
        np_text = get_np(text[find_pattern.end():])
        if np_text:
            print(np_text)
            find_np_recursive(np_text, pattern)


def main():
    np_p = "\(NP (\(.*?\))\)"
    np_start_p = "\(NP "
    tree = etree.parse('data/nlp_coref.txt.xml')
    for depend in tree.getroot().iterfind(".//parse"):
        find_np_recursive(depend.text, np_start_p)


if __name__ == '__main__':
    main()
