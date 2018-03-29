# -*- coding : utf-8 -*-
import pycountry
import re
from itertools import islice
from chap_09 import ch09_80
"""81. 複合語からなる国名への対処"""


def make_country_list():
    # 国名一覧取得
    remove_strings = """ .,!?;:()[]\'\""""
    country_list = []
    for country in list(pycountry.countries):
        name = country.name
        if len(name.split()) > 1:
            if len(name.split(',')) > 1:
                name = " ".join([part_name.strip(remove_strings) for part_name in name.split(",")[::-1]])
                # print(name)
            country_list.append(name)
        try:
            official = country.official_name
            if len(official.split()) > 1:
                if len(official.split(',')) > 1:
                    official = " ".join([part_name.strip(remove_strings) for part_name in official.split(",")[::-1]])
                    # print(official)
            country_list.append(official)
        except AttributeError:
            # official_nameがない場合attribute_errorになる
            pass
    return country_list


def main(data_path):
    country_pattern = re.compile("|".join(make_country_list()))
    with open('data/enwiki-81.txt', 'w')as fw:
        for line in islice(ch09_80.shaping_corpus(data_path),10):
            for find_pattern in country_pattern.finditer(line):
                line = re.sub(find_pattern.group(0), find_pattern.group(0).replace(' ', '_'), find_pattern.string)
            fw.write(line+"\n")


if __name__ == '__main__':
    main("/Users/shirai/100knock-2017/shihono/sh_chap09/data/enwiki-20150112-400-r100-105752.txt.bz2")