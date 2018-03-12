#!/bin/sh
echo 'make data/col1.txt'
cut -f1 ./../data/hightemp.txt > ./../data/col1.txt
echo 'make data/col2.txt'
cut -f1 ./../data/hightemp.txt > ./../data/col2.txt
