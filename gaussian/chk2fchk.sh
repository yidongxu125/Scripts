#!/bin/bash

total=$(ls -1 *.chk | wc -l)
count=0
for inf in *.chk; do
    count=$((count+1))
    echo "Processing file $count of $total: $inf"
    formchk ${inf}
done
