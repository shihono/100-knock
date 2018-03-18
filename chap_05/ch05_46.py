# -*- coding : utf-8 -*-
from chap_05 import ch05_41
"""46. 動詞の格フレーム情報の抽出"""
save_path = 'data/46_kaku.txt'


def main():
    chunk_data = ch05_41.create_chunk_list_by_cabocha()
    with open(save_path, 'w')as f:
        for chunk_list in chunk_data:
            for chunk in chunk_list:
                for kaku_list in chunk.get_kaku_pattern46(chunk_list):
                    f.write(' '.join(kaku_list) + '\n')
    print("save file into {}".format(save_path))


if __name__ == '__main__':
    main()