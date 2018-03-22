# -*- coding : utf-8 -*-
import json
import redis
conn_1 = redis.StrictRedis(host='localhost', port=6379,db=1)


def main():
    cnt = 0
    with open("data/artist.json", "r")as f:
        for line in f:
            artist_data = json.loads(line)
            if "tags" in artist_data.keys():
                # print(artist_data)
                if cnt < 10:
                    print("{} : {}".format(artist_data['name'], artist_data['tags']))
                for tags in artist_data['tags']:
                    conn_1.hset(artist_data['name'], tags['value'], tags['count'])
                cnt += 1
    print("Process End: Count{}".format(cnt))


if __name__ == '__main__':
    main()
