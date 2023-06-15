#!/bin/bash

# Version 1.0
# By Yidongxu
# 创建保存结果的文本文件 "Gibbs.txt"
> Gibbs.txt

# 遍历所有的 ".out" 文件
for inf in *.out
do
  # 提取 "Thermal correction to Gibbs Free Energy" 数值并保存到 "Gibbs.txt" 中
  tac "$inf" | grep -m 1 "Thermal correction to Gibbs Free Energy" | tr -cd '[:digit:].-' | awk '{print $1}' >> Gibbs.txt

  # 输出文件名
  echo "$inf"
done
