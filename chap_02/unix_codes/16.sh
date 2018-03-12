#!/bin/sh
echo "split files $1"
split -l $1 ./../data/hightemp.txt data/split