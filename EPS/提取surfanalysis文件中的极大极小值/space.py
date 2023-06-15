# version 1.0
# by yidongxu
#用法：multiwfn处理后，导出的txt会在极大值和极小值前面加一个*，影响脚本16和17的数据提取，需要首先对*号进行删除并用空格代替
import os

# 获取当前文件夹下的所有子文件夹
subfolders = [f.path for f in os.scandir('./') if f.is_dir()]

# 定义要替换的字符*变空格
old_char = '*'
new_char = ' '

# 遍历每个子文件夹，并读取其中的surfanalysis.txt文档进行替换
for folder in subfolders:
    surfanalysis_path = os.path.join(folder, 'surfanalysis.txt')
    if os.path.exists(surfanalysis_path):
        with open(surfanalysis_path, 'r') as f:
            content = f.read()
        content = content.replace(old_char, new_char)
        with open(surfanalysis_path, 'w') as f:
            f.write(content)
