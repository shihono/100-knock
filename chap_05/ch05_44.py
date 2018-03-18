# -*- coding : utf-8 -*-
import pydot
from chap_05 import ch05_41
"""44. 係り受け木の可視化"""


def relate_edge(chunk_list):
    """係り受け木のedgeを作る"""
    edges = []
    for phrase in chunk_list:
        if phrase.dst != -1:
            edges.append(tuple([''.join(phrase.show_bunsetsu()), ''.join(chunk_list[phrase.dst].show_bunsetsu())]))
    return edges


def main(sentence_idx:int):
    chunk_data = ch05_41.create_chunk_list_by_cabocha()
    chunk_sent_list = chunk_data[sentence_idx]
    rg = pydot.graph_from_edges(relate_edge(chunk_sent_list))
    rg.write_png('img/44edges.png', prog='dot')


if __name__ == '__main__':
    main(8)
