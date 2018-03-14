# -*- coding: utf-8 -*-
import sys
import os
import subprocess
import pprint
from collections import Counter

""" 10 から 19"""
if not os.path.isfile("./data/hightemp.txt"):
    cmd = '''curl http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt >> ./data/hightemp.txt '''
    cmd_line = subprocess.check_output(cmd, shell=True).decode('utf-8', errors='replace')

with open("./data/hightemp.txt", "r")as f:
    line = f.readlines()


def ch02_10_main():
    """10. 行数のカウント"""
    print(len(line))


def ch02_11_main():
    """11. タブをスペースに置換"""
    pprint.pprint([s.replace('\t',' ') for s in line])


def ch02_12_main():
    """12. 1列目をcol1.txtに，2列目をcol2.txtに保存"""
    col1 = []
    col2 = []
    for word in line:
        words = word.split('\t')
        col1.append(words[0])
        col2.append(words[1])
    pprint.pprint(col1[:10])
    pprint.pprint(col2[:10])
    return col1, col2


def ch02_13_main():
    """13. col1.txtとcol2.txtをマージ"""
    col1, col2 = ch02_12_main()
    col1col2 = [w1 + '\t' + w2 + '\t\n' for w1, w2 in zip(col1, col2)]
    pprint.pprint(col1col2[:10])


def ch02_14_main(n:int):
    """14. 先頭からN行を出力"""
    pprint.pprint([line[t] for t in range(n)])


def ch02_15_main(n:int):
    """15. 末尾のN行を出力"""
    pprint.pprint([line[len(line) - n + t] for t in range(n)])


def ch02_16_main(n:int):
    """16. ファイルをN分割する"""
    pprint.pprint([line[len(line) // n * c: len(line) // n * (c + 1) - 1] for c in range(n)])


def ch02_17_main():
    """17. １列目の文字列の異なり"""
    col1 = [l.split()[0] for l in line]
    pprint.pprint(list(set(col1)))
    print(len(list(set(col1))))


def ch02_18_main():
    """18. 各行を3コラム目の数値の降順にソート"""
    pprint.pprint(sorted([l.split() for l in line], key=lambda x: float(x[2]), reverse=True))


def ch02_19_main():
    """19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる"""
    col1 = [l.split()[0] for l in line]
    pprint.pprint(Counter(col1).most_common())


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ['10','11', '12', '13',  '17', '18', '19']:
        eval('ch02_{}_main'.format(sys.argv[1]))()
    elif len(sys.argv) > 2 and sys.argv[1] == '14':
        ch02_14_main(n=int(sys.argv[2]))
    elif len(sys.argv) > 2 and sys.argv[1] == '15':
        ch02_15_main(n=int(sys.argv[2]))

    elif len(sys.argv) > 2 and sys.argv[1] == '16':
        ch02_16_main(n=int(sys.argv[2]))
    else:
        print("Please specify the problem number;the argument should be between 10 and 19")

