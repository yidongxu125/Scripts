#!/bin/bash

# 获取当前文件夹中所有.gjf文件的文件名
gjf_files=$(ls *.gjf)

# 遍历每个.gjf文件
for gjf_file in $gjf_files; do
    # 删除以 Tv 开头的行，然后添加两行空行
    sed -i '/^Tv/d' $gjf_file
    echo -e "\n\n" >> $gjf_file
done

