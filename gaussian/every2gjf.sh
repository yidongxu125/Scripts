#!/bin/bash

# Version 1.0
# By Yidongxu
# 支持out,chk，fchk,mol,mol2,cif

icc=0
nfile=$(ls -1 *.out *.chk *.fchk *.mol *.mol2 *.cif 2>/dev/null | wc -l)
for inf in *.out *.chk *.fchk *.mol *.mol2 *.cif; do
    if [ -f "$inf" ]; then
        ((icc++))
        echo "Converting ${inf} to ${inf%.*}.gjf ... ($icc of $nfile)"
        Multiwfn "$inf" <<EOF > /dev/null
100
2
10
${inf%.*}.gjf
0
q
EOF
    fi
done