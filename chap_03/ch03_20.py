# -*- coding : utf-8 -*-
import gzip
import json
"""20. JSONデータの読み込み"""


def main_20():
    with gzip.open('./data/jawiki-country.json.gz', 'rt') as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                return data['text'].split('\n')


if __name__ == '__main__':
    print(len(main_20()))
