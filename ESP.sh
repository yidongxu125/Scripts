#!/bin/bash

# Version 2.2
# By yidongxu
# 对当前文件夹下所有的fchk文件进行分析，并生成对应的文件夹，保存density.cub，mol.pdb，surfanalysis.pdb，surfanalysis.txt等文件；
# 把导出的文件重命名修改成作者默认的文件名，另外导出了每个原子的表面电势供方便画图
# 相当于Multiwfn软件的ESPiso和ESPext脚本，如果如需要其他文件修改下方的数字即可。

echo "Version 2.2,Script edit By yidongxu"
echo "Script is begining,please wait...."

# 获取当前文件夹路径
current_dir=$(pwd)

# 删除当前文件夹下老文件
rm -f *.cub
rm -f *.pdb
rm -f *.txt

count=0 # 统计处理的 .fchk 文件数量
for inf in *.fchk; do
    if [ -f "$inf" ]; then
        count=$((count+1)) # 处理一个 .fchk 文件，数量加一
        dir="${inf%.*}"
        if [ ! -d "$dir" ]; then
            mkdir "$dir"
        fi
        echo "Processing ${inf} ($count of $(ls *.fchk | wc -l))"
        Multiwfn "$inf" <<EOF > ${dir}/medinfo.txt
5
1
3
2
0
5
12
2
2
0
12
0
11
n
-1
3
0.15
0
5
mol.pdb
6
1
2
-1
-1
q
EOF
     mv  density.cub ${dir}/density1.cub
     mv  totesp.cub ${dir}/ESP1.cub
     mv  vtx.pdb ${dir}/vtx1.pdb
     mv  mol.pdb ${dir}/mol1.pdb
     mv  surfanalysis.txt ${dir}
     mv  surfanalysis.pdb ${dir}/surfanalysis.pdb
     echo " ${inf} ($count of $(ls *.fchk | wc -l)) OK " 
    fi
done
echo "所有计算已完成,接下来提取每个原子的表面电势值"

# 遍历当前文件夹下的所有子文件夹
for dir in "$current_dir"/*/; do
  # 检查是否存在 medinfo.txt 文件
  if [ -f "$dir/medinfo.txt" ]; then
    echo "处理文件夹: $dir"

    # 提取目标数据行之间的内容并保存到新文件
    sed -n '/Note: Minimal and maximal value below are in kcal\/mol/,/If outputting the surface facets to locsurf.pdb in current folder? By which you can visualize local surface via third-part visualization program such as VMD (y\/n)/p' "$dir/medinfo.txt" > "$dir/atomsurface.txt"

    echo "已导出提取文件: $dir/atomsurface.txt"
  fi
done
echo "恭喜您!所有计算和导出完毕,OK"
# 运行完成之后会发邮件给你，修改自己邮箱，-s '邮件主题' 最前面前述是内容
echo "all gaussian run over" | mail -s 'gaussian2 EPS over' XXX@163.com