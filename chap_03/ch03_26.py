# -*- coding : utf-8 -*-
import re
from chap_03 import ch03_25

"""26. 強調マークアップの除去"""
def main_26():
    info_box = ch03_25.main_25()
    link = re.compile("(\[\[)([^[\]]*)(]])")

    infoboxl = {}
    for key, value in info_box.items():
        ml = link.search(value)
        if ml:
            infoboxl[key] = link.sub(ml.group(2), value)
        else:
            infoboxl[key] = value
    return infoboxl


if __name__ == '__main__':
    info_box = main_26()
    for k,v in info_box.items():
        print("{}:{}".format(k, v))
