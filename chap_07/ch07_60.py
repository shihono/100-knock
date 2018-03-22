# -*- coding : utf-8 -*-
import json
import redis
# redisと接続
conn = redis.StrictRedis(host='localhost', port=6379, db=0)
pipe = conn.pipeline()


def main():
    with open("data/artist.json", "r")as f:
        for line in f:
            artist_data = json.loads(line)
            # areaがjsonにない場合があるので確かめてからデータベースにいれる
            if "area" in artist_data:
                pipe.set(artist_data['name'], artist_data['area'], nx=True)


if __name__ == '__main__':
    main()