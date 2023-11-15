#!/bin/bash

# Version 3.1
# By yidognxu
# 生成静电势数值的 txt 和 pdb 格式，并将结果移动到对应的文件夹中

#删除当前文件夹下老文件
rm -f *.txt
rm -f *.pdb

count=0 # 统计处理的 .fchk 文件数量
for inf in *.fchk; do
    if [ -f "$inf" ]; then
        count=$((count+1)) # 处理一个 .fchk 文件，数量加一
        dir="${inf%.*}"
        if [ ! -d "$dir" ]; then
            mkdir "$dir"
        fi
        echo "Processing ${inf} ($count of $(ls *.fchk | wc -l))"
        Multiwfn "$inf" <<EOF > /dev/null
12
3
0.15
0
5
${dir}/mol.pdb
6
2
1
-1
-1
q
EOF
     cp -R surfanalysis.txt surfanalysis.pdb vtx.pdb ${dir}
      
    fi
done