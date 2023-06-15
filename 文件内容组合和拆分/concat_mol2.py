# version 1.0
# by yidongxu
# 用法：使得当前文件夹下所有的mol2文件组合成单个mol2文件，用来供堆积相似性分析
import os

# 获取当前目录
cur_dir = os.getcwd()
# 确保当前目录中没有all.mol2文件
if os.path.exists(cur_dir + '/all.mol2'):
    os.remove(cur_dir + '/all.mol2')

# 储存所有文件内容的列表
contents = []

# 找到所有.mol2文件并读取它们的内容
for filename in os.listdir(cur_dir):
    # 只考虑mol2文件
    if filename.endswith('.mol2'):
        with open(filename, 'r') as f:
            contents.append(f.read())
        contents.append('\n\n')

# 将所有文件内容组合成一个字符串
contents_str = ''.join(contents)

# 将所有文件内容写入all.mol2文件
with open('all.mol2', 'w') as f:
    f.write(contents_str)
