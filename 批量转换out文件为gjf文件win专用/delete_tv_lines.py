import os

# By Yidongxu
# Version 1.0
# 使用说明:删除带有周期性格式的文件转换成gjf文件后文末带有Tv开头的标记
# 获取当前文件夹中所有.gjf文件的文件名
gjf_files = [filename for filename in os.listdir('.') if filename.endswith('.gjf')]

# 遍历每个.gjf文件
for gjf_file in gjf_files:
    with open(gjf_file, 'r') as f:
        lines = f.readlines()  # 读取文件的每一行内容

    # 删除以 Tv 开头的行
    lines = [line for line in lines if not line.startswith('Tv')]

    # 在文件末尾加入两行空行
    lines.append('\n')
    lines.append('\n')

    # 覆盖当前文件
    with open(gjf_file, 'w') as f:
        f.writelines(lines)
