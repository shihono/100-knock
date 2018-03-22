# -*- coding : utf-8 -*-
from lxml import etree


def main():
    tree = etree.parse('./data/nlp_coref.txt.xml')
    # 参照表現の取得
    repre_sentence_dict = {}
    for element in tree.getroot().iterfind(".//coreference"):
        represent = None
        for mention in element.iterfind(".//mention"):
            if mention.attrib.get('representative') is not None:
                represent = mention.findtext('text')
            else:
                # print([item.text for item in element.iter()])
                repre_sentence_dict[int(mention.findtext('sentence'))] = [int(mention.findtext('start')),
                                                                          int(mention.findtext('end')),
                                                                          mention.findtext('text'),
                                                                          represent]
    output_sentences = []
    for sentence in tree.getroot().iterfind(".//document/sentences/sentence"):
        sentence_id = int(sentence.attrib.get('id'))
        if sentence_id in repre_sentence_dict.keys():
            for item in sentence.iterfind("./tokens/token"):
                token_id = int(item.attrib.get('id'))
                # 参照開始地点で"["を足す
                if token_id == repre_sentence_dict[sentence_id][0]:
                    output_sentences.append("[")
                output_sentences.append(item.find('word').text)
                if token_id == repre_sentence_dict[sentence_id][1] - 1:
                    # 参照の終了地点で"]"を足す+ 参照表現のtextをappend
                    #print(repre_sentence_dict[sentence_id][2])
                    output_sentences.append("] ({})".format(repre_sentence_dict[sentence_id][3]))
    print(" ".join(output_sentences[:50]))


if __name__ == '__main__':
    main()
