#!/bin/bash

lang=$1
prob_num=$(printf "%03d" $2)
file="solutions/$prob_num/$prob_num"

case $lang in
  js) node "$file.js";;
  py) python "$file.py";;
  *) echo 'unknown';;
esac