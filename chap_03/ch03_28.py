# -*- coding : utf-8 -*-
import re
from chap_03 import ch03_27
"""28. MediaWikiマークアップの除去"""


def main_28():
    info_box = ch03_27.main_27()
    #markup = re.compile("\{\{(?P<c>[^{}]*)\}\}")
    markup = re.compile(r'(\[|<)(.+)(\]|>)')
    infobox28 = {}

    for k, v in info_box.items():
        infobox28[k] = markup.sub('', v)
        # re.sub('<ref name:"imf-statistics-gdp" />',''infobox28[k])
    return infobox28


if __name__ == '__main__':
    infobox = main_28()
    for k, v in infobox.items():
        print("{}:{}".format(k, v))
