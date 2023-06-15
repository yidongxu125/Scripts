#!/bin/bash

# Version 1.0
# By Yidongxu

# 删除已存在的 "getGall.txt" 文件
rm -f getGall.txt

# 遍历所有的 ".out" 文件
i=1
for inf in *.out
do
  echo "Processing ${inf} ..."
  echo "${inf}" >> getGall.txt

  # 从 "Gibbs.txt" 文档中获取第 n 行数字
  n=$(sed -n "${i}p" Gibbs.txt)

  # 从 "scf.txt" 文档中获取第 i 行数字
  m=$(sed -n "${i}p" scf.txt)

  # 使用获取的数字替换命令中的 "0.975" 和 "-300"
  ./Shermo "${inf}" -sclZPE "${n}" -E "${m}" -ilowfreq 2 | grep "Sum of electronic energy and thermal correction to G:" | cut -d: -f 2 >> getGall.txt

  # 增加索引
  i=$((i+1))
done