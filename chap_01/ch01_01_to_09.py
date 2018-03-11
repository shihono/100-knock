# -*- coding: utf-8 -*-
import pprint
import sys
import numpy as np
""" 100knock 01　から 09　までのコード"""


def ch01_01_main(pata="パタトクカシーー"):
    """01.「パタトクカシーー」"""
    print(pata[1::2])


def ch01_02_main(patrol="パトカー ", taxi= "タクシー"):
    """02.「パトカー」＋「タクシー」＝「パタトクカシーー」"""
    print(''.join([p + t for p, t in zip(patrol, taxi)]))


def ch01_03_main():
    """03. 円周率"""
    en_sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    sent_len_list = [len(word) for word in en_sent.split()]
    print(en_sent)
    pprint.pprint(sent_len_list)


def ch01_04_main():
    """04. 元素記号"""
    element_sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
                   "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    print(element_sent)
    one_index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    element_dict = {(item[:1] if (index in one_index) else item[:2]): index
                    for index, item in enumerate(element_sent.split(), start=1)}
    pprint.pprint(element_dict)


def ch01_05_main(n=2, seq="I am an NLPer", is_chara=False):
    """05. n-gram
    * n : bi-gram
    * seq: sequence
    * is_chara : if True, return chara n-gram, default is word n-gram
    """
    if not is_chara:
        return [seq[i:i + n] for i in range(len(seq) - n + 1)]
    else:
        seq = seq.split()
        return [seq[i:i + n] for i in range(len(seq) - n + 1)]


def ch01_06_main(x="paraparaparadise", y="paragraph"):
    """06. 集合"""
    x_bigram = set(ch01_05_main(n=2, seq=x))
    y_bigram = set(ch01_05_main(n=2, seq=y))
    print("union : {},\nintersection : {},\ndiff : (x-y){} (y-x){}".format(x_bigram&y_bigram, x_bigram|y_bigram,
                                                                             x_bigram-y_bigram, y_bigram-x_bigram))
    print("se in {} : {}\nse in {} : {}".format(x, 'se' in x_bigram, y, 'se' in y_bigram))


def ch01_07_main(x=12, y="気温", z=22.4):
    """07. テンプレートによる文生成"""
    template = "{}時の{}は{}"
    return template.format(x, y, z)


def cipher(moji:str):
    """for chapter01 08 function"""
    return ''.join((chr(219-ord(m))) if m.islower() else m for m in moji)


def ch01_08_main(seq=None):
    """08. 暗号文"""
    if seq is None:
        seq = "This is example And 8 o'clock."
    print("encipher : {}".format(cipher(seq)))
    print("decipher : {}".format(cipher(cipher(seq))))


def ch01_09_main(seq=None):
    """09. Typoglycemia"""
    if seq is None:
        seq = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    typo_list = seq.split(" ")
    result_typo = []
    for typo in typo_list:
        if len(typo)>4:
            numbers = np.arange(start=1, stop=len(typo)-1)
            np.random.shuffle(numbers)
            result_typo.append((",".join([typo[0]]+[typo[idx] for idx in numbers]+ [typo[-1]])).replace(",", ""))
        else:
            result_typo.append(typo)
    print(seq)
    print(" ".join(result_typo))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        eval('ch01_0{}_main'.format(sys.argv[1]))()
    else:
        print("Please specify the problem number;the argument should be between 1 and 9")