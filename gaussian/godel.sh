#!/bin/bash

icc=0
nfile=$(ls ./*.gjf | wc -l)

for inf in *.gjf; do
    ((icc++))
    echo "Running ${inf} .., (${icc} of ${nfile})"
    time g16 < ${inf} > ${inf//gjf/out}
    echo "${inf} has finished"
    echo
done

# 清空 scratch 文件夹中的内容
rm -rf /home/admin/g16/scratch/*

# 运行完成之后会发邮件给你，修改自己邮箱，-s '邮件主题' 最前面前述是内容
echo "all gaussian run over" | mail -s 'gaussian2 go over' yidongxu125@163.com
