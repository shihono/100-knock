# -*- coding : utf-8 -*-
from pymongo import MongoClient
from pymongo import IndexModel, ASCENDING, DESCENDING
import json
# database の立ち上げ mkdir -p data/db mongod --dbpath data/db
client = MongoClient('localhost',27017)
db = client['artist_db']
collection = db['artist_collection']


def main():
    with open("data/artist.json", 'r')as f:
        for line in f:
            json_data = json.loads(line)
            collection.insert_one(json_data)
    # indexの作成
    index1 = IndexModel([('name', ASCENDING)])
    index2 = IndexModel([('aliases.name', ASCENDING)])
    index3 = IndexModel([('tags.value', DESCENDING)])
    index4 = IndexModel([('rating.value', DESCENDING)])
    collection.create_indexes([index1, index2, index3, index4])

    print(list(collection.index_information()))


def main_65():
    print(collection.find_one({'name': 'Queen'}))


def main_67(alias:str):
    for cursor in collection.find({'aliases.name': alias}):
        print(cursor)


def main_68():
    for cursor in collection.find({'tags.value': 'dance'}).sort('rating.count', DESCENDING)[:10]:
        print(cursor['name'])
        if cursor['rating']:
            print(cursor['rating'])


if __name__ == '__main__':
    main()
