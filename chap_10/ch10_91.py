# -*- coding : utf-8 -*-
from itertools import takewhile, dropwhile
"91. アナロジーデータの準備"


def main():
    flag = False
    with open('./work/91_analogy.txt', 'w')as fw:
        with open('./data/questions-words.txt', 'r')as f:
            for line in f:
                if 'family' in line:
                    flag = True
                elif flag and ':' in line:
                    flag = False
                elif flag:
                    fw.write(line)


if __name__ == '__main__':
    main()