# -*- coding : utf-8 -*-
from xml.etree import ElementTree
"""54. 品詞タグ付け"""


def trace_postag(parent,output_pos_list):
    for node in list(parent):
        # print(node.tag)
        if node.tag=="token":
            for word,lemma,pos in zip(node.iter('word'),node.iter('lemma'),node.iter('POS')):
                #print(child.text)
                output_pos_list.append("{}\t{}\t{}".format(word.text,lemma.text, pos.text))
        trace_postag(node, output_pos_list)


def main():
    tree = ElementTree.parse('./data/nlp.txt.xml')
    root = tree.getroot()
    output_pos = []
    trace_postag(root, output_pos)
    print(output_pos[:10])


if __name__ == '__main__':
    main()
