#!/bin/bash

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

#-----------------------------------------------------

prob_num=$(printf "%03d" $1)
prob_title=${problems[$1]}

mkdir "solutions/$prob_num"
cp "solutions/001/001.js" "solutions/$prob_num/$prob_num.js"
cp "solutions/001/001.py" "solutions/$prob_num/$prob_num.py"

sed -i -e "s/001/$prob_num/g" "solutions/$prob_num/$prob_num.js"
sed -i -e "s/001/$prob_num/g" "solutions/$prob_num/$prob_num.py"

sed -i -e "s/Multiples of 3 and 5/$prob_title/g" "solutions/$prob_num/$prob_num.js"
sed -i -e "s/Multiples of 3 and 5/$prob_title/g" "solutions/$prob_num/$prob_num.py"

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