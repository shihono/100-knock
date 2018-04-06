# -*- coding : utf-8 -*-
from itertools import takewhile, dropwhile
"91. アナロジーデータの準備"


def main2():
    # takewhileとdropwhileを使う場合
    with open('./data/questions-words.txt', 'r')as f:
        for line in takewhile(lambda y: y == ': family\n' or not y.startswith(':'),
                              dropwhile(lambda x: x != ': family\n', f)):
            print(line.strip())


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