#!/bin/bash

lang=$1
prob_num=$(printf "%03d" $2)
path="solutions/$prob_num"
cd $path

case $lang in
  js) node "$prob_num.js";;
  py) python "$prob_num.py";;
  *) echo 'unknown';;
esac