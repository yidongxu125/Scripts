# version 1.0
# by yidongxu
# 用法：删除有些文件是由gview生成后在文件前面会多出来好多行问题，把@<TRIPOS>MOLECULE提到最前面
import os

# 获取当前文件夹路径
path = os.getcwd()

# 遍历当前文件夹中所有的mol2文件
for filename in os.listdir(path):
    if filename.endswith(".mol2"):
        # 打开每个mol2文件并读取内容
        with open(filename, "r") as f:
            lines = f.readlines()
            
        # 获取@<TRIPOS>MOLECULE所在的行数
        mol_line = -1
        for i in range(len(lines)):
            if "@<TRIPOS>MOLECULE" in lines[i]:
                mol_line = i
                break
        
        # 如果找到了@<TRIPOS>MOLECULE，则将其前面的所有行都删除
        if mol_line > 0:
            new_lines = []
            new_lines.append(lines[mol_line])
            new_lines.extend(lines[mol_line+1:])
            
            # 写入修改后的内容到原文件中
            with open(filename, "w") as f:
                f.writelines(new_lines)