#!/bin/bash

#  Version 1.0
#  By Yidongxu

# 删除已存在的 "getGall.txt" 文件
rm -f getGall.txt
rm -f scf.txt
rm -f Gibbs.txt

# 创建保存结果的文本文件
> scf.txt
> Gibbs.txt
> getGall.txt

# 切换到下一级文件夹 "sp"
cd sp

# 遍历所有的 ".out" 文件
for inf in *.out
do
  echo "Processing ${inf} ..."

  # 提取 "SCF Done" 数值并保存到当前文件夹中的 scf.txt 中
  tac "$inf" | grep -m 1 "SCF Done" | awk '{print $5}' >> ../scf.txt

  # 输出文件名
  echo "$inf"
done

# 返回到上一级文件夹
cd ..

# 遍历所有的 ".out" 文件
for inf in *.out
do
  echo "Processing ${inf} ..."

  # 提取 "SCF Done" 数值并保存到当前文件夹中的 scf.txt 中
  tac "$inf" | grep -m 1 "Thermal correction to Gibbs Free Energy" | tr -cd '[:digit:].-' | awk '{print $1}' >> Gibbs.txt

  # 输出文件名
  echo "$inf"
done

# 遍历所有的 ".out" 文件
i=1
for inf in *.out
do
  echo "Processing ${inf} ..."

  # 将当前文件名追加到 getGall.txt 文件中，并将数值与文件名对齐
  printf "%-30s" "${inf}" >> getGall.txt

  # 从 Gibbs.txt 文档中获取第 i 行数字
  n=$(sed -n "${i}p" Gibbs.txt)

  # 从 scf.txt 文档中获取第 i 行数字
  m=$(sed -n "${i}p" scf.txt)

  # 使用获取的数字替换命令中的 "0.975" 和 "-300"
  /home/admin/Shermo_2.3.6/./Shermo "${inf}" -sclZPE "${n}" -E "${m}" -ilowfreq 2 | grep "Sum of electronic energy and thermal correction to G:" | cut -d: -f 2 | awk '{$1=$1};1' >> getGall.txt

  # 增加索引
  i=$((i+1))

  # 输出文件名
  echo "$inf"
done