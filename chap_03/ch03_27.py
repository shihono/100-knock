# -*- coding : utf-8 -*-
import re
from chap_03 import ch03_26
"""28. MediaWikiマークアップの除去"""


def main_27():
    info_box = ch03_26.main_26()
    link = re.compile("(\[\[)([^[\]]*)(]])")

    infobox27 = {}

    for key, value in info_box.items():
        ml = link.search(value)
        if ml:
            infobox27[key] = link.sub(ml.group(2), value)
        else:
            infobox27[key] = value
    return infobox27


if __name__ == '__main__':
    infobox = main_27()
    for k, v in infobox.items():
        print("{}:{}".format(k, v))
