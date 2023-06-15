#!/bin/bash

# Version 1.0
# By Yidongxu

shopt -s nullglob

file_count=0
total_files=$(find . -type f -name "*.gjf" | wc -l)

for dir in */
do
  cd "$dir"

  for inf in *.gjf
  do
    ((file_count++))
    echo "Running ${inf} ... (${file_count} of ${total_files})"
    time g16 < "${inf}" > "${inf%.*}.out"
    echo "${inf} has finished"
    echo
  done

  cd ..
done
