# -*- coding : utf-8 -*-
from lxml import etree
"""53. Tokenization"""

"""
Stanford core NLPを用いて nlp.txt.xml を出力
java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP 
-annotators tokenize,ssplit,pos,lemma,ner,parse -file nlp.txt -outputFormat xml
"""


def main():
    word_list = [word.text for word in etree.parse('./data/nlp.txt.xml').getroot().iter('word')]
    print(word_list[:5])


if __name__ == '__main__':
    main()