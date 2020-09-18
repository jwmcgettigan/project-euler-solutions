#!/bin/bash

prob_num=$1

problems=()
delimiter="##"
while read line; do
  array=()
  s=$line$delimiter
  while [[ $s ]]; do
    array+=( "${s%%"$delimiter"*}" );
    s=${s#*"$delimiter"};
  done;
  problems+=( "${array[1]}" )
done < "problems.txt"

echo ${problems[1]}