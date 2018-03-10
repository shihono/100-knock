# -*- coding: utf-8 -*-

"""
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""


def reverse_string(ex_string :str):
    return ex_string[::-1]


def reverse_string_not_good(ex_string : str):
    ex_list = list(ex_string)
    return "".join(reversed(ex_list))


if __name__ == '__main__':
    example = "stressed"
    print(reverse_string(ex_string=example))
    print(reverse_string_not_good(example))