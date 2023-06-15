#!/bin/bash

# Version 1.0
# By Yidongxu
# �������������ı��ļ� "Gibbs.txt"
> Gibbs.txt

# �������е� ".out" �ļ�
for inf in *.out
do
  # ��ȡ "Thermal correction to Gibbs Free Energy" ��ֵ�����浽 "Gibbs.txt" ��
  tac "$inf" | grep -m 1 "Thermal correction to Gibbs Free Energy" | tr -cd '[:digit:].-' | awk '{print $1}' >> Gibbs.txt

  # ����ļ���
  echo "$inf"
done
