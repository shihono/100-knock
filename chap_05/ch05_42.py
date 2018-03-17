# -*- coding : utf-8 -*-
from chap_05 import ch05_41
"""42. 係り元と係り先の文節の表示"""


def main(sentence_idx:int):
    chunk_data = ch05_41.create_chunk_list_by_cabocha()
    chunk_sent_list = chunk_data[sentence_idx]
    for chunk in chunk_sent_list:
        if chunk.dst != -1 and chunk.is_contain_pos("名詞") and chunk_sent_list[chunk.dst].is_contain_pos("動詞"):
            print(''.join(chunk.show_bunsetsu()), end="\t")
            print(''.join(chunk_sent_list[chunk.dst].show_bunsetsu()))


if __name__ == '__main__':
    main(9)