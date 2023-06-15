#version 2.1.0
# by yidongxu
#用发：修改mol2文件中内部名字和文件名不相同问题，修改成和文件名一样
import os

# 获取当前文件夹路径
path = os.getcwd()

# 新建“修改mol”文件夹
if not os.path.exists(path + "/修改mol"):
    os.mkdir(path + "/修改mol")

# 遍历当前文件夹中所有的mol2文件
for filename in os.listdir(path):
    if filename.endswith(".mol2"):
        # 打开每个mol2文件并读取内容
        with open(filename, "r") as f:
            lines = f.readlines()

        # 设置最大查找行数为20
        max_lines = 20
        mol_line = -1
        for i in range(max_lines):
            # 搜索@<TRIPOS>MOLECULE所在的行数
            if "@<TRIPOS>MOLECULE" in lines[i]:
                mol_line = i
                break

        # 检查文件名是否和@<TRIPOS>MOLECULE的下一行内容相同
        if mol_line != -1 and mol_line < len(lines) - 1:
            name_line = lines[mol_line + 1].strip().split()[-1]
            file_name_without_suffix = filename.split(".")[0]
            if file_name_without_suffix != name_line:
                # 如果不相同则修改@<TRIPOS>MOLECULE的下一行内容
                new_name_line = " ".join(lines[mol_line + 1].strip().split()[:-1]) + " " + file_name_without_suffix + "\n"
                lines[mol_line + 1] = new_name_line

                # 写入修改后的内容到新文件中
                with open(path + "/修改mol/" + filename, "w") as f:
                    f.writelines(lines)