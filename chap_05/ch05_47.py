# -*- coding : utf-8 -*-
from chap_05 import ch05_41
"""47. 機能動詞構文のマイニング"""
save_path = 'data/47_kaku.txt'


def get_kaku_pattern47(chunk_list):
    for idx, chunk in enumerate(chunk_list):
        if chunk.is_contain("pos1", "サ変接続") and chunk.is_contain("surface", "を") and len(chunk.morphs) < 3:
            if chunk_list[chunk.dst].is_contain("surface", "する"):
                print(''.join(chunk.show_base()), end="\t")
                print(''.join(chunk_list[chunk.dst].show_bunsetsu()))


def main():
    chunk_data = ch05_41.create_chunk_list_by_cabocha()
    for chunks in chunk_data:
        get_kaku_pattern47(chunks)


if __name__ == '__main__':
    main()