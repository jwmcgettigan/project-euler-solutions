#!/bin/bash

for i in {1..22}
do
  prob_num=$(printf "%03d" $i)
  #mkdir "solutions/$prob_num"
  #mv "python/$prob_num.py" "solutions/$prob_num"
  #mv "javascript/$prob_num.js" "solutions/$prob_num"
  #mv "notes/$prob_num.txt" "solutions/$prob_num"
done

mv "resources/p022_names.txt" "solutions/022"