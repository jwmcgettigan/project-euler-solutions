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

probNum=$(printf "%03d" $1)
probTitle=${problems[$1]}
fileTypes=('.js' '.py' '.txt')

mkdir "solutions/$probNum"
for fileType in "${fileTypes[@]}"; do
  cp "solutions/000/000$fileType" "solutions/$probNum/$probNum$fileType"
  sed -i -e "s/###/$probNum/g" "solutions/$probNum/$probNum$fileType"
  sed -i -e "s/TITLE/$probTitle/g" "solutions/$probNum/$probNum$fileType"
done

placeholderText="The folder this file is in contains templates
for easing the creation of new files for each problem."
sed -i -e "s/$placeholderText//g" "solutions/$probNum/$probNum.txt"

: '
for i in {1..22}
do
  probNum=$(printf "%03d" $i)
  #mkdir "solutions/$probNum"
  #mv "python/$probNum.py" "solutions/$probNum"
  #mv "javascript/$probNum.js" "solutions/$probNum"
  #mv "notes/$probNum.txt" "solutions/$probNum"
done

#mv "resources/p022_names.txt" "solutions/022"
# '