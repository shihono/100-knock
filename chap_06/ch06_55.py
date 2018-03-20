# -*- coding : utf-8 -*-
from lxml import etree
"""55. 固有表現抽出"""


def main():
    for token in etree.parse('./data/nlp.txt.xml').getroot().iter('token'):
        if token.find('NER').text == 'PERSON':
            print(token.find('word').text)


if __name__ == '__main__':
    main()
