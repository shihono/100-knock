# -*- coding : utf-8 -*-
import pycountry
from chap_09 import ch09_81
from chap_10 import ch10_90
"96. 国名に関するベクトルの抽出"


def get_one_word_country():
    # １単語の国名は保存していなかったので新たに取得し直す
    for country in list(pycountry.countries):
        name = country.name
        if len(name.split()) < 2:
            yield name


def main(is_return=None):
    w2v_vec = ch10_90.load_w2v_data()
    country_list = ch09_81.make_country_list() + list(get_one_word_country())
    country_vec = {}
    for country in country_list:
        try:
            country_vec[country] = w2v_vec[country]
        except KeyError:
            pass
            # print("{} is not in vocab".format(country))
    if is_return:
        return country_vec
    else:
        with open("./work/96_country_vec.txt", 'w')as f:
            for k, v in country_vec.items():
                f.write("{},{}\n".format(k, v))
        print("write ./work/96_country_vec.txt")


if __name__ == '__main__':
    main()