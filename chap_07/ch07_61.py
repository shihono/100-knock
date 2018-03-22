# -*- coding : utf-8 -*-
import redis
# from chap_07 import ch07_60
conn = redis.StrictRedis(host='localhost', port=6379, db=0)


def main():
    print(conn.get('Alexander Purkart'))


if __name__ == '__main__':
    main()
