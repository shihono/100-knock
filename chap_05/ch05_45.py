# -*- coding : utf-8 -*-
import subprocess
from chap_05 import ch05_41
"""45. 動詞の格パターンの抽出"""
save_path = 'data/45_kaku.txt'


def main():
    chunk_data = ch05_41.create_chunk_list_by_cabocha()
    with open(save_path, 'w')as f:
        for chunk_list in chunk_data:
            for chunk in chunk_list:
                for kaku_list in chunk.get_kaku_pattern(chunk_list):
                    f.write(' '.join(kaku_list) + '\n')
    print("save file into {}".format(save_path))
    cmd = '''cat {} |sort | uniq -c | sort -rn '''.format(save_path)
    output_cmd = subprocess.check_output(cmd, shell=True).decode('utf-8', errors='replace').strip().split('\n')
    print(output_cmd[:10])


if __name__ == '__main__':
    main()