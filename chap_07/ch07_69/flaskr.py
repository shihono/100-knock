from flask import Flask, render_template,request
from pymongo import MongoClient, DESCENDING
import logging

# databaseが立ち上がってる前提
# mongod -dbpath data/dv で立ち上がる
app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['artist_db']
collection = db['artist_collection']


@app.route('/')
def index_page():
    logging.info('index page')
    return render_template('index.html', no_query=True)


@app.route('/post', methods=['GET','POST'])
def home_page():
    # result_name = mongo.db.users.find({'aliases.name':'オアシス'})
    if request.method == 'POST':
        logging.info('post query')
        if request.form['artist']:
            query = request.form['artist']
            field = 'name'
        elif request.form['aliases']:
            query = request.form['aliases']
            field = 'aliases.name'
        elif request.form['tag']:
            query = request.form['tag']
            field = 'tags.value'
        else:
            return render_template('index.html', no_query=True)
        result = collection.find({field: query}).sort('rating.count', DESCENDING).limit(10)
        logging.info(result)
        return render_template('index.html', query=query, result_cursor=result)

if __name__ == '__main__':
    app.debug = True
    app.run()
