#!/usr/bin/env bash
mongo
use artist_db
db.artist_collection.find({'area':'Japan'}).count()