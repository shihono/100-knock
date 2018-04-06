# -*- coding : utf-8 -*-
from itertools import islice
from chap_10 import ch10_90
"94. WordSimilarity-353での類似度計算"


def add_sim_353(result_data_name, wv):
    with open('./work/{}'.format(result_data_name),'w')as fw:
        with open('./data/combined.csv','r')as fr:
            for line in islice(fr,1,None):
                set_data = line.split(',')
                try:
                    sim = wv.similarity(set_data[0],set_data[1])
                except KeyError:
                    sim = 0
                fw.write("{},{}\n".format(line.strip(),sim))
        print("write at ./work/{}".format(result_data_name))


def main():
    wv = ch10_90.load_w2v_data()
    add_sim_353('94_w2v.csv', wv)


if __name__ == '__main__':
    main()