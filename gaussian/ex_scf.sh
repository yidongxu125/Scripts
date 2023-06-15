#!/bin/bash

# Version 1.0
# By Yidongxu

# 创建保存结果的文本文件"scf.txt"
> scf.txt

# 切换到下一级文件夹"sp"
cd sp

# 遍历所有的".out"文件
for inf in *.out
do
  # 提取"SCF Done"数值并保存到上一级文件夹中的"scf.txt"中
  tac $inf | grep -m 1 "SCF Done" | awk '{print $5}' >> ../scf.txt

  # 输出文件名
  echo $inf
done
