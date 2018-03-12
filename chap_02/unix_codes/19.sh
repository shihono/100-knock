#!/bin/sh
cut -f1 ./../data/hightemp.txt|sort |uniq -c | sort -rn