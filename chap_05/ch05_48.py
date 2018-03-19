# -*- coding : utf-8 -*-
from chap_05 import ch05_41
"""48. 名詞から根へのパスの抽出"""


# 再帰させてdstをたどる
def find_dst(chunk_list, chunk):
    # print("is_dst:{}".format(chunk))
    if chunk.dst != -1:
        pathlist = ["".join(chunk.show_bunsetsu())]
        pathlist.extend(find_dst(chunk_list, chunk_list[chunk.dst]))
        return pathlist
    else:
        return ["".join(chunk.show_bunsetsu())]


def get_path48(line_idx):
    chunk_data = ch05_41.create_chunk_list_by_cabocha()
    chunk_line = chunk_data[line_idx]
    for chunk in chunk_line:
        if chunk.is_contain_pos("名詞") and chunk.dst != -1:
            print(" -> ".join(find_dst(chunk_line, chunk)))


if __name__ == '__main__':
    # 吾輩はここで始めて人間というものを見た
    get_path48(5)