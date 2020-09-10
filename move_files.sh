#!/bin/bash

prob_num=$(printf "%03d" $1)
mkdir "solutions/$prob_num"
cp "solutions/001/001.js" "solutions/$prob_num/$prob_num.js"
cp "solutions/001/001.py" "solutions/$prob_num/$prob_num.py"
sed -i -e "s/001/$prob_num/g" "solutions/$prob_num/$prob_num.js"
sed -i -e "s/001/$prob_num/g" "solutions/$prob_num/$prob_num.py"

: '
for i in {1..22}
do
  prob_num=$(printf "%03d" $i)
  #mkdir "solutions/$prob_num"
  #mv "python/$prob_num.py" "solutions/$prob_num"
  #mv "javascript/$prob_num.js" "solutions/$prob_num"
  #mv "notes/$prob_num.txt" "solutions/$prob_num"
done

#mv "resources/p022_names.txt" "solutions/022"
# '