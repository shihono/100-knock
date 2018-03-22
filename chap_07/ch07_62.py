# -*- coding : utf-8 -*-
import redis
conn = redis.StrictRedis(host='localhost', port=6379, db=0)


def main():
    jp_count = 0
    for key in conn.keys("*"):
        if conn.get(key) == b'Japan':
            if jp_count < 20:
                print(key.decode())
            jp_count += 1
    print(jp_count)


if __name__ == '__main__':
    main()